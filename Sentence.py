from Source import *


# Subclass of Source - text is raw text from document
# - text: raw string from sentence
# - scores: list of Score objects between this sentence and all queries
class Sentence:

        def __init__(self, text, features):
            Source.__init__(self, features)
            self.text = text
            self.scores = []

