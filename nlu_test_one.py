from InformationRetrieval import *


username = "f2291678-5b43-445c-8cfb-0890b3a47969"
password = "vk65ROc1bvte"

# Create InformationRetrieval instance to handle analysis
retrieval = InformationRetrieval(username=username,
                                 password=password)

# Add the list of wanted features
retrieval.add_features_and_weights(['keywords', 'concepts', 'entities'], [1, 1, 1])
#
# # Add a test query
retrieval.add_source("Gambling should be outlawed in the United States", SourceType.query)
retrieval.add_source("The existence of God is undeniable.", SourceType.query)
# retrieval.add_source("God God God God Existence of God God Existence", SourceType.query)
# retrieval.add_source("Gun laws are too strict in America", SourceType.query)
# retrieval.add_source("Dogs are a great pet especially for Veterans", SourceType.query)
# retrieval.add_source("Cats are not good pets for little kids", SourceType.query)
# retrieval.add_source("Taxes in the United States should be lowered", SourceType.query)
# retrieval.add_source("Taxes in Mexico should be lowered", SourceType.query)
#
# # Add a test document
# retrieval.add_source("http://gun-control.procon.org", SourceType.document)
# retrieval.add_source("https://en.wikipedia.org/wiki/African-American_Civil_Rights_Movement_(1954–1968)",
#                      SourceType.document)
# retrieval.add_source("https://en.wikipedia.org/wiki/Dog", SourceType.document)
# retrieval.add_source("https://en.wikipedia.org/wiki/Martin_Luther_King_Jr.", SourceType.document)
# retrieval.add_source("https://www.washingtonpost.com/business/economy/washington-braces-for-details-of-trumps-tax-reform-plan/2017/04/25/1fba8b30-29df-11e7-a616-d7c8a68c1a66_story.html?utm_term=.edfd96806ae5", SourceType.document)
# retrieval.add_source("https://americansfortaxfairness.org/tax-fairness-briefing-booklet/fact-sheet-taxing-wealthy-americans/", SourceType.document)
# retrieval.add_source("http://www.worldwide-tax.com/mexico/mexico_taxes.asp", SourceType.document)
#
# retrieval.score_sources()
#
# retrieval.display_scores()

# print(retrieval.queries[0].analysis['categories'])
# print(retrieval.documents[0].analysis['categories'])
#
#
# print(retrieval.queries[0].analysis['keywords'])
# print(retrieval.documents[0].analysis['keywords'])

# file_gambling = open("Gambling", "r+")
# gambling = file_gambling.read()

# file_guns = open("Gun_control", "r+")
# guns = file_guns.read()

file_god = open("sentences/Existence_of_God", "r+", encoding="utf-8")
file_gambling = open("sentences/Gambling", "r+", encoding="utf-8")

god = file_god.read()
gambling = file_gambling.read()


#
# retrieval.add_source(gambling, SourceType.document)
# retrieval.add_source(guns, SourceType.document)
retrieval.add_source(gambling, SourceType.document)
retrieval.add_source(god, SourceType.document)


# for passage in retrieval.documents[0].passages:
#     print(passage.text)


sentences = retrieval.get_summary(n_docs=1, n_passages=5, n_sentences=5)

for query_index, query in enumerate(retrieval.queries):
    print("Query: ", query.text)
    for sentence in sentences[query_index]:
        print("\tText:", sentence.text)
        print("\t\tScore:", sentence.scores[query_index].weighted_score(), "\n\n")


