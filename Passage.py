from Source import *
from SourceType import *
from Sentence import *

from nltk.tokenize import sent_tokenize

import re


# Subclass of Source - text is raw text from document
# - text: raw string from passage
# - scores: list of Score objects between this document and all queries
# - sentences: list of Sentence objects that hold all sentences from this passage
class Passage(Source):

        def __init__(self, text, features):
            Source.__init__(self, features, SourceType.passage)
            self.text = text
            self.sentences = self.get_sentences()

        # Returns list of Sentence objects and stores them in self.sentences
        def get_sentences(self):
            # split_sentences = re.split('[.!?]', self.text)
            split_sentences = sent_tokenize(self.text)
            sentences = []
            for sentence in split_sentences:
                # self.sentences.append(Sentence(text = sentence, features = self.features))
                sentences.append(Sentence(text = sentence, features = self.features))
            return sentences


        # Returns subset of self.sentences with top n scoring passages for each query
        def get_highest_sentences(self, n):
            highest_sentences = []
            for query_index in range(len(self.scores)):
                highest_sentences.append(self.highest_sentences_for_query(n, query_index))

        # Returns list of n highest scoring passages for this query
        def highest_sentences_for_query(self, n, query_index):
            highest_sentences = sorted(self.sentences,
                                       key=lambda sentence: sentence.scores[query_index].weighted_score(),
                                       reverse=True)
            return highest_sentences[:n]

