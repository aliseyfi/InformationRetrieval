import watson_developer_cloud

from SourceType import *
from Source import *
from Document import *
from Query import *
from Score import *
from Feature import *


class InformationRetrieval:

    def __init__(self, username, password):
        self.nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(version='2017-02-27',
                                                                         username=username,
                                                                         password=password)
        self.features = []
        self.queries = []
        self.documents = []

    def add_features_and_weights(self, feature_names, weights):
        problem_features = []
        for feature_number, name in enumerate(feature_names):
            weight = 0
            if feature_number < len(weights):
                weight = weights[feature_number]
            feature = Feature(name, weight)
            if feature.element is not None:
                self.features.append(feature)
            else:
                problem_features.append(name)
        if len(problem_features) > 0:
            print("Problem features:")
            for feature in problem_features:
                print(feature)

    def analyze_source(self, source, kind):
        if SourceType.query == kind:
            return self.nlu.analyze(text=source.text, features=self.feature_elements())
        elif SourceType.document == kind:
            return self.nlu.analyze(url=source.url, features=self.feature_elements())

    def add_source(self, data, kind):
        if SourceType.query == kind:
            query = Query(text=data, features=self.feature_elements())
            query.analysis = self.analyze_source(source=query, kind=SourceType.query)
            self.queries.append(query)

        elif SourceType.document == kind:
            document = Document(url=data, features=self.feature_elements())
            document.analysis = self.analyze_source(source=document, kind=SourceType.document)
            self.documents.append(document)

    # Compares sources by calculating the score for the 2 sources for all features
    # - the calculated score is added to the given query's score list
    def compare_sources(self, query_index, document_index, features):
        query = self.queries[query_index]
        document = self.documents[document_index]
        score = Score(query, document, features)
        score.calculate_feature_scores()
        return score

    # Generates updated scores for every query and document pair
    # - uses the current list of features
    def score_sources(self):
        for query_index in range(len(self.queries)):
            updated_scores = []
            for document_index in range(len(self.documents)):
                updated_scores.append(self.compare_sources(query_index, document_index, self.features))
            self.queries[query_index].scores = updated_scores

    # Returns array of only the feature elements
    def feature_elements(self):
        return [feature.element for feature in self.features]

    # Returns array of only the feature names
    def feature_names(self):
        return [feature.name for feature in self.features]

    # Returns array of only the feature weights
    def feature_weights(self):
        return [feature.weight for feature in self.features]

    # Prints out feature scores for each query-document pairing
    def display_scores(self):
        for query_index, query in enumerate(self.queries):
            print("Query %i: %s" % (query_index, query.text))
            for document_index, score in enumerate(query.scores):
                print("\tDocument %i: %s" % (document_index, self.documents[document_index].url))
                for feature_name in score.scores:
                    print("\t\t", feature_name, score.scores[feature_name])
                print("\t\t", "total", score.total_score())


