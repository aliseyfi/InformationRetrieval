
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
                score += self.element_score(query_element, document_element, feature)

        return score

    # Calculates score for individual elements of query-document pair analysis
    def element_score(self, query_element, document_element, feature):
        # These keys should be different for different features
        if feature.name == "keywords":
            return query_element['relevance'] * document_element['relevance'] * \
                   self.element_similarity(query_element, document_element, feature)


    # Calculates the similarity score between the query text and the document text
    def element_similarity(self, query_element, document_element, feature):
        # Keys for this need to be different for different features
        return 1
