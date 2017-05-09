from Source import *


# Subclass of Source - text is raw text from document
# - text: raw string from document
# - scores: list of Score objects between this document and all queries
# - passages: list of Passage objects that hold all passages from this document
class Document:

    def __init__(self, text, features):
        Source.__init__(self, features)
        self.text = text
        self.scores = []
        self.passages = get_passages(self)

    # Calculates the relevancy score of the document with the given query and returns the score
    def relevance_score(self, query):


    # Calculates relevancy score of document for all queries
    # - result is returned and stored in self.scores
    def calculate_scores(self, queries):
        scores = []
        for query in queries:
            scores.append(self.relevance_score(query))
        self.scores = scores
        return scores


    # Returns list of Passage objects and stores them in self.passages
    def get_passages(self):
        split_passages = re.split('\n\n', self.text)
        for paragraph in split_passages:
            self.passages.append(Passage(text=paragraph, features=self.features))

    # Returns subset of self.passages with top n scoring passages for each query
    def get_highest_passages(self, n):
        highest_passages = []
        for query_index in range(len(self.scores)):
            highest_passages.append(self.highest_passages_for_query(n, query_index))

    # Returns list of n highest scoring passages for this query
    def highest_passages_for_query(self, n, query_index):
        highest_passages = sorted(self.passages, key=lambda passage: passage.scores[query_index].weighted_score())
        return highest_passages[:n]
