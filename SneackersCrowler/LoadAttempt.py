from collections import UserDict
from datetime import datetime

class CGood(UserDict):
    def __init__(self):
        super().__init__(self)
        self["Name"] = None
        self["Uri"] = None
        self["Date"] = None
        self["ImgUriList"] = list()
    
class CLoadAttempt(UserDict):
    def __init__(self, SourceName, CountToLoad):  
        super().__init__(self)
        self["CountToLoad"] = CountToLoad
        self["Source"] = SourceName      
        self["Date"] = datetime.utcnow()
        self["ErrorList"] = list()




