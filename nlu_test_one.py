from InformationRetrieval import *


username = "450b4230-5e4c-4547-900d-3b6ee9347541"
password = "Ec8m5yA0YBEx"

# Create InformationRetrieval instance to handle analysis
retrieval = InformationRetrieval(username=username,
                                 password=password)

# Add the list of wanted features
retrieval.add_features(['keywords', 'concepts', 'entities', 'categories'])

# Add a test query
retrieval.add_source("Gun should be outlawed in the United States", SourceType.query)
print(retrieval.queries[0].analysis['keywords'])

# Add a test document
retrieval.add_source("http://gun-control.procon.org", SourceType.document)
print(retrieval.documents[0].analysis['keywords'])

