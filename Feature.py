import watson_developer_cloud.natural_language_understanding.features.v1 as features

class Feature:

    def __init__(self, name):
        self.name = name
        self.element = Feature.map_feature(name)

    @staticmethod
    def map_feature(name):
        feature_name_mappings = {'keywords': features.Keywords(),
                                 'entities': features.Entities(),
                                 'concepts': features.Concepts(),
                                 'categories': features.Categories()}
        if name in feature_name_mappings:
            return feature_name_mappings[name]
        else:
            print("Invalid feature name")
            return None
