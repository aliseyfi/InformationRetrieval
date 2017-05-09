from Source import *


# Subclass for sentence manipulation and scoring
# - text: raw text
# - scores: list of score objects for a sentence


class Sentence:

    def __init__(self, text, features):
        Source.__init__(self, features)
        self.text = text
        self.scores = []
