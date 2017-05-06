
class Score:

    def __init__(self, query, document, features):
        self.query = query
        self.document = document
        self.features = features
        self.scores = {}

    # Calculates aggregate score for this query-document pair by individually
    # calculating the scores for each given feature
    def calculate_feature_scores(self):
        score = 0
        for feature in self.features:
            self.scores[feature] = self.calculate_score(feature)

    # Calculates score between query-document pair for the given feature
    def calculate_score(self, feature):
        query_analysis = self.query.analysis[feature]
        document_analysis = self.document.analysis[feature]
        score = 0

        for query_element in query_analysis:
            for document_element in document_analysis:
                score += self.element_score(query_element, document_element)

        return score

    # Calculates score for individual elements of query-document pair analysis
    def element_score(self, query_element, document_element):
        return query_element['relevance'] * document_element['relevance'] * text_similarity(query_element['text'],
                                                                                            document_element['text'])
    # Calculates the similarity score between the query text and the document text
    def text_similarity(self, query_text, document_text):
        return 1
