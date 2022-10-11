from selenium import webdriver
import NikeCrowler

#create Chrome Driver without images
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe", chrome_options=chrome_options)


nikeCrowler = NikeCrowler.CNikeCrowler(driver)
loadAttempt = nikeCrowler.GetTodayGoodList()

driver.close()