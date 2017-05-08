# DeepQA Final

# InformationRetrieval
Carries out entire process of Information Retrieval including
document/query addition, analysis, and scoring

- features: List of Feature objects used for analysis and scoring

- queries: List of Query objects used for analysis and scoring

- documents: List of Document objects used for analysis and scoring


# Score
Handles all scoring between query document pairs

- query: query source that this score is for

- document: document source that this score is for

- features: list of feature objects to use for the scoring

- scores: dictionary of key=feature.name, value=score


# SourceType
Enumeration for different types of Sources

- document: evidence based source with text derived from URL

- query: question based source with text derived from string


# Source
Superclass for Document and Query

- features: list of Feature objects to use for this source

- analysis: returned analysis from running NLU analysis


# Query
Subclass of Source - text derived from given text string

- scores is a list of Score objects representing the scores between the query and each document


# Document
Subclass of Source - text is derived from the given URL


# Feature
Holds all relevant information about a feature

- name: string name representation

- element: Watson feature representation

- weight: weight to use for feature when calculating score
