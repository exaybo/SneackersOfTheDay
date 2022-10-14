import dbm
from selenium import webdriver
import NikeCrowler
import LoadAttempt
import DbManager
import json

'''normal mode'''
##driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Chrome() #after add to PATH and reboot

'''headless mode, no images, no 3d'''
'''https://developer.chrome.com/blog/headless-chrome/'''
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1500,1200")
options.add_argument("no-sandbox")
options.add_argument("disable-dev-shm-usage")
options.add_argument("disable-gpu")
options.add_argument("log-level=3")
options.add_argument("disable-3d-apis")

prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

try:
    nikeAttempt = LoadAttempt.CLoadAttempt("Nike", 11)
    nikeImageList = list()
    nikeSneackerList = list()
    nikeCrowler = NikeCrowler.CNikeCrowler(driver)
    nikeCrowler.GetTodayGoodList(nikeAttempt, nikeSneackerList, nikeImageList)


    #nikeAttempt["ErrorList"].append("err1")
    #g = LoadAttempt.CGood()
    #g["Name"] = "air max"
    #g["Uri"] = "uri sneakers"
    #g["ImgUriList"].append("uri image1")
    #nikeList = list()
    #nikeList.append(g)

    dbMgr = DbManager.CDbManager.get_instance()
    dbMgr.SaveAttempt(nikeAttempt)
    dbMgr.SaveSneakers(nikeSneackerList)
    dbMgr.SaveBinImageList(nikeImageList)

    attempts = dbMgr.GetAttempts()
    #sneakers = dbMgr.GetSneackers()

    print( str(attempts) )
except Exception as e:
    print(vars(e))
finally:
    driver.close()


#build image
# docker build -t sneackers_crowler .

#run
# docker run --rm -d -p 27017:27017 mongo

#run in command line mode
# docker run -it --entrypoint=/bin/bash sneackers_crowler

#run mongo
# docker run --rm -d -p 27017:27017 mongo