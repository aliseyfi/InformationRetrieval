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
retrieval.add_source("Taxes in the United States should be lowered", SourceType.query)
retrieval.add_source("Taxes in Mexico should be lowered", SourceType.query)

# Add a test document
retrieval.add_source("http://gun-control.procon.org", SourceType.document)
retrieval.add_source("https://en.wikipedia.org/wiki/African-American_Civil_Rights_Movement_(1954–1968)",
                     SourceType.document)
retrieval.add_source("https://en.wikipedia.org/wiki/Dog", SourceType.document)
retrieval.add_source("https://en.wikipedia.org/wiki/Martin_Luther_King_Jr.", SourceType.document)
retrieval.add_source("https://www.washingtonpost.com/business/economy/washington-braces-for-details-of-trumps-tax-reform-plan/2017/04/25/1fba8b30-29df-11e7-a616-d7c8a68c1a66_story.html?utm_term=.edfd96806ae5", SourceType.document)
retrieval.add_source("https://americansfortaxfairness.org/tax-fairness-briefing-booklet/fact-sheet-taxing-wealthy-americans/", SourceType.document)
retrieval.add_source("http://www.worldwide-tax.com/mexico/mexico_taxes.asp", SourceType.document)

retrieval.score_sources()

retrieval.display_scores()

# print(retrieval.queries[0].analysis['categories'])
# print(retrieval.documents[0].analysis['categories'])
#
#
# print(retrieval.queries[0].analysis['keywords'])
# print(retrieval.documents[0].analysis['keywords'])
