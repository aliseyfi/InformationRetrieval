
class Score:

    def __init__(self, query, document, feature_names):
        self.query = query
        self.document = document
        self.feature_names = feature_names
        self.scores = {}

    # Sums scores for all features and returns the result
    def aggregate_score(self):
        return sum(self.scores.values())

    # Calculates aggregate score for this query-document pair by individually
    # calculating the scores for each given feature
    def calculate_feature_scores(self):
        for feature in self.feature_names:
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
        # These keys should be different for different features
        return query_element['relevance'] * document_element['relevance'] * self.text_similarity(query_element['text'],
                                                                                                 document_element['text'])
    # Calculates the similarity score between the query text and the document text
    def text_similarity(self, query_text, document_text):
        # Keys for this need to be different for different features
        return 1
