import LoadAttempt

class CDbManager(object):


    def SaveAttempt(self, todayAttempt):
        print("LoadAttempt:")
        print("Source = ", todayAttempt.Source)
        print("Errors = ", str(todayAttempt.ErrorList))
        print("Uris loaded = ", len(todayAttempt.GoodList))
        if len(todayAttempt.GoodList) > 0:
            print("First good name = ", todayAttempt.GoodList[0].Name)



