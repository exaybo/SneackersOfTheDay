from datetime import date

class CGood:
    Name = ""
    ImgUriList = list()

class CLoadAttempt(object):
    def __init__(self, SourceName, countToLoad):        
        self.countToLoad = countToLoad
        self.Source = SourceName      
        self.Date = date.today()
        self.ErrorList = list()
        self.GoodList = list()




