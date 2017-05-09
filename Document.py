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


    # Katherine: get_passages()
    # - returns list of Passage objects and stores them in self.passages
    def get_passages(self):
        split_passages = re.split('\n\n', self.text)
        for paragraph in split_passages:
            self.passages.append(Passage(text = paragraph, features = self.features)

    # Returns subset of self.passages with top n scoring passages
    def get_highest_passages(self, n):
        highest_passages = []
        for query_index in range(len(self.scores)):
            highest_passages.append(self.highest_passages_for_query(n, query_index))

    def highest_passages_for_query(self, n, query_index):
        highest_passages = sorted(self.passages, key=lambda passage: passage.scores[query_index])
        return highest_passages[:n]
