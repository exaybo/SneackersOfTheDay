from collections import UserDict
from datetime import datetime

import urllib.request

class CGood(UserDict):
    def __init__(self):
        super().__init__(self)
        self["Name"] = None
        self["Uri"] = None
        self["Date"] = None
        self["ImgUriList"] = list()

class CBinImage(UserDict):
    def __init__(self):
        super().__init__(self)
        self["ImgUri"] = None
        self["ImgBin"] = None

    def loadBinImage(self, uri):
        resource = urllib.request.urlopen(uri)
        self["ImgBin"] = resource.read()
        self["ImgUri"] = uri

    
class CLoadAttempt(UserDict):
    def __init__(self, SourceName, CountToLoad):  
        super().__init__(self)
        self["CountToLoad"] = CountToLoad
        self["CountOfLoaded"] = 0
        
        self["Source"] = SourceName      
        self["Date"] = datetime.utcnow()
        self["ErrorList"] = list()




