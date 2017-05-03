import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as features

from SourceType import *
from Source import *
from Document import *
from Query import *


class InformationRetrieval:

    def __init__(self, username, password):
        self.nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(version='2017-02-27',
                                                                         username=username,
                                                                         password=password)
        self.features = []
        self.queries = []
        self.documents = []

    def add_features(self, feature_names):
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

    #def compare_sources(self, source_one, source_two, feature_name):


    #def score_sources(self, features, weights):

