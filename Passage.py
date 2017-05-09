from Source import *


# Subclass for passage and sentence manipulation and scoring
# - text: raw text
# - scores: list of score objects
# - sentences: list of sentences in a passage

class Passage:

    def __init__(self, text, features):
        Source.__init__(self, features)
        self.text = text
        self.scores = []
        self.sentences = []

    # Katherine: get_sentences()
        # returns list sentence objects and stores them in self.sentences

    # returns subset of sentences with highest n scores
    def get_highest_passages(self, n):
        highest_sentences = []
        for query_index in range(len(self.scores)):
            highest_sentences.append(self.highest_sentences_for_query(n, query_index))

    def highest_sentences_for_query(self, n, query_index):
        highest_sentences = sorted(self.sentences, key = lambda sentence: sentence.scores[query_index].weighted_score())
        return highest_sentences[:n]