from Source import *


# Subclass of Source - text is raw text from document
# - text: raw string from passage
# - scores: list of Score objects between this document and all queries
# - sentences: list of Sentence objects that hold all sentences from this passage
class Passages:

        def __init__(self, text, features):
                    Source.__init__(self, features)
                            self.text = text
                                    self.scores = []
                                            self.sentences = get_sentences(self)


        # - returns list of Sentence objects and stores them in self.sentences
        def get_sentences(self):
            split_sentences = re.split('[.!?]', self.text)
            for sentence in split_sentences:
                self.sentences.append(Sentence(text = sentence, features = self.features)

