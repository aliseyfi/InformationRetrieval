

# Superclass for Document and Query
# - features: list of Feature objects to use for this source
# - analysis: returned analysis from running NLU analysis
class Source:

    def __init__(self, features):
        self.features = features
        self.analysis = {}

