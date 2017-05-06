import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as features

from SourceType import *
from Source import *
from Document import *
from Query import *
from Score import *


class InformationRetrieval:

    def __init__(self, username, password):
        self.nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(version='2017-02-27',
                                                                         username=username,
                                                                         password=password)
        self.features = []
        self.feature_names = []
        self.queries = []
        self.documents = []

    def add_features(self, feature_names):
        self.feature_names = feature_names
        feature_name_mappings = {'keywords': features.Keywords(),
                                 'entities': features.Entities(),
                                 'concepts': features.Concepts(),
                                 'categories': features.Categories()}
        problem_features = []
        for feature_number, name in enumerate(feature_names):
            if name in feature_name_mappings:
                self.features.append(feature_name_mappings[name])
            else:
                problem_features.append(name)
        if len(problem_features) > 0:
            print("Problem features:")
            for feature in problem_features:
                print(feature)

    def analyze_source(self, source, kind):
        if SourceType.query == kind:
            return self.nlu.analyze(text=source.text, features=self.features)
        elif SourceType.document == kind:
            return self.nlu.analyze(url=source.url, features=self.features)

    def add_source(self, data, kind):
        if SourceType.query == kind:
            query = Query(text=data, features=self.features)
            query.analysis = self.analyze_source(source=query, kind=SourceType.query)
            self.queries.append(query)

        elif SourceType.document == kind:
            document = Document(url=data, features=self.features)
            document.analysis = self.analyze_source(source=document, kind=SourceType.document)
            self.documents.append(document)

    # Compares sources by calculating the score for the 2 sources for all features
    # - the calculated score is added to the given query's score list
    def compare_sources(self, query_index, document_index, feature_names):
        query = self.queries[query_index]
        document = self.documents[document_index]
        score = Score(query, document, feature_names)
        score.calculate_feature_scores()
        return score

    # Generates updated scores for every query and document pair
    # - uses the current list of features
    def score_sources(self):
        for query_index in range(len(self.queries)):
            updated_scores = []
            for document_index in range(len(self.documents)):
                updated_scores.append(self.compare_sources(query_index, document_index, self.feature_names))
            self.queries[query_index].scores = updated_scores

    # Prints out feature scores for each query-document pairing
    def display_scores(self):
        for query_index, query in enumerate(self.queries):
            print("Query %i" % query_index)
            for document_index, score in enumerate(query.scores):
                print("\tDocument %i" % document_index)
                for feature_name in score.scores:
                    print("\t\t", feature_name, score.scores[feature_name])


