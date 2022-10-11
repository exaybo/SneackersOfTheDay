from selenium import webdriver
import NikeCrowler
import LoadAttempt
import DbManager

#create Chrome Driver without images
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe", chrome_options=chrome_options)

nikeAttempt = LoadAttempt.CLoadAttempt("Nike", 1)

nikeCrowler = NikeCrowler.CNikeCrowler(driver)
nikeCrowler.GetTodayGoodList(nikeAttempt)

dbMgr = DbManager.CDbManager()
dbMgr.SaveAttempt(nikeAttempt)

driver.close()