from Source import *


# Subclass of Source - text is derived from the given URL
# - url: web url where Source text can be found
class Document:

    def __init__(self, url, features):
        Source.__init__(self, features)
        self.url = url

