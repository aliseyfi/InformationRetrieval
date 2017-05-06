from nltk.corpus import wordnet as wn


class Score:

    def __init__(self, query, document, features):
        self.query = query
        self.document = document
        self.features = features
        self.scores = {}

    # Sums scores for all features and returns the result
    def aggregate_score(self):
        return sum(self.scores.values())

    # Calculates aggregate score for this query-document pair by individually
    # calculating the scores for each given feature
    def calculate_feature_scores(self):
        for feature in self.features:
            self.scores[feature.name] = self.calculate_score(feature)

    # Calculates score between query-document pair for the given feature
    def calculate_score(self, feature):
        query_analysis = self.query.analysis[feature.name]
        document_analysis = self.document.analysis[feature.name]
        score = 0

        for query_element in query_analysis:
            for document_element in document_analysis:
                score += Score.element_score(query_element, document_element, feature)

        return score

    # Calculates score for individual elements of query-document pair analysis
    @staticmethod
    def element_score(query_element, document_element, feature):
        # These keys should be different for different features
        if feature.name == "keywords":
            return query_element['relevance'] * document_element['relevance'] * \
                   Score.element_similarity(query_element, document_element, feature)

    # Calculates the similarity score between the query text and the document text
    @staticmethod
    def element_similarity(query_element, document_element, feature):
        # Keys for this need to be different for different features
        if feature.name == "keywords":
            return Score.similarity(query_element['text'], document_element['text'])
        return 1

    # Calculates similarity between query and document text
    # - uses WordNet Wu and Palmer similarity score for each query-document word pairing
    @staticmethod
    def similarity(query_text, document_text):
        score = 0
        query_words = query_text.split(" ")
        document_words = document_text.split(" ")

        for query_word in query_words:
            for document_word in document_words:
                score += Score.wu_palmer_similarity(query_word, document_word)
        return score

    # Converts given words into WordNet objects
    @staticmethod
    def wordnet_representation(word):
        synset = wn.synsets(word)
        if synset is None or len(synset) == 0:
            return None
        return wn.synsets(word)[0]

    # Calculates Wu and Palmer similarity for the two given raw text words
    @staticmethod
    def wu_palmer_similarity(word1, word2):
        wordnet_word1 = Score.wordnet_representation(word1)
        wordnet_word2 = Score.wordnet_representation(word2)
        if wordnet_word1 is None or wordnet_word2 is None:
            return 0
        similarity = wn.wup_similarity(wordnet_word1, wordnet_word2)
        if similarity is None:
            return 0
        return similarity
