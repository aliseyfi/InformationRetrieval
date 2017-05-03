# InformationRetrieval
Final project for DeepQA


InformationRetrieval Class:

self.queries: list of Query objects that contain information about all queries
self.documents: list of Document objects that contain information about the appropriate document

#TODO
self.scores: list of Score objects that contain information about scores

Score Class:

self.document: document the score is for
self.query: query the score is for
self.score: aggregate score for this document query pairing

// Maybe store components that contributed to the aggregate score

