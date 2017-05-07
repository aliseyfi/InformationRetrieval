from InformationRetrieval import *


username = "450b4230-5e4c-4547-900d-3b6ee9347541"
password = "Ec8m5yA0YBEx"

# Create InformationRetrieval instance to handle analysis
retrieval = InformationRetrieval(username=username,
                                 password=password)

# Add the list of wanted features
retrieval.add_features_and_weights(['keywords', 'entities', 'concepts', 'categories'], [1, 1, 1, 50])

# Add a test query
retrieval.add_source("Gun should be outlawed in the United States", SourceType.query)
retrieval.add_source("The civil rights movement was a turning point in the US", SourceType.query)
retrieval.add_source("Dogs are a great pet especially for Veterans", SourceType.query)
retrieval.add_source("Cats are not good pets for little kids", SourceType.query)

# Add a test document
retrieval.add_source("http://gun-control.procon.org", SourceType.document)
retrieval.add_source("https://en.wikipedia.org/wiki/African-American_Civil_Rights_Movement_(1954–1968)",
                     SourceType.document)
retrieval.add_source("https://en.wikipedia.org/wiki/Dog", SourceType.document)
retrieval.add_source("https://en.wikipedia.org/wiki/Martin_Luther_King_Jr.", SourceType.document)

retrieval.score_sources()

retrieval.display_scores()

# print(retrieval.queries[0].analysis['categories'])
# print(retrieval.documents[0].analysis['categories'])
#
#
# print(retrieval.queries[0].analysis['keywords'])
# print(retrieval.documents[0].analysis['keywords'])
