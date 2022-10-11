from selenium import webdriver
import NikeCrowler
import LoadAttempt
import DbManager

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
    nikeAttempt = LoadAttempt.CLoadAttempt("Nike", 1)

    nikeCrowler = NikeCrowler.CNikeCrowler(driver)
    nikeCrowler.GetTodayGoodList(nikeAttempt)

    dbMgr = DbManager.CDbManager()
    dbMgr.SaveAttempt(nikeAttempt)
finally:
    driver.close()

#docker run -it --entrypoint=/bin/bash