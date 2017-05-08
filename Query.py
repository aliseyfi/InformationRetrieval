from Source import *


# Subclass of Source - text derived from given text string
# - scores is a list of Score objects representing the scores between
# the query and each document
class Query:

    def __init__(self, text, features):
        Source.__init__(self, features)
        self.text = text
        self.scores = []

