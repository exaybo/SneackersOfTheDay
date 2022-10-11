from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import LoadAttempt

class CNikeCrowler(object):
    def __init__(self, selDriver):
        self.driver = selDriver

    def CloseInfoPopups(self):
        '''close info popups such as cookie agreement'''
        #close cookie agreement
        try:
            cookieAgree = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-var='acceptBtn1']"))
            )
            cookieAgree.click()
        except:
            pass
    
        #close any windows
        try:
            otherWidows = self.driver.find_elements_by_css_selector("[data-var='closeButton']")
            for wnd in otherWidows:
                wnd.click()
        except:
            pass

    def OpenGoodsPage(self, typeOfGoodsLink = "a[data-path='men:shoes']"):
        '''open page of type of goods'''
        manShoes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, typeOfGoodsLink))
        )
        manShoesUri = manShoes.get_attribute('href');
        self.driver.get(manShoesUri)

    def GetGoodsUriList(self):
        '''load uris of goods on page'''        
        #press End to load more goods
        for i in range(3):
            actions = webdriver.ActionChains(self.driver)
            actions.send_keys('\ue010')
            actions.perform()
            self.driver.implicitly_wait(5)

        #Goods
        goodLinks = self.driver.find_elements_by_css_selector("div[data-product-position] a[aria-label]")

        #Goods uris
        goodUris = [g.get_attribute('href') for g in goodLinks]
        return goodUris

    def GetDetailedOfGood(self, uri):
        good = LoadAttempt.CGood()
        #navigate to random good
        #driver.get(goodUris[random.randint(0,len(goodUris))])
        self.driver.get(uri)

        #show good detailed images
        aGoodDetailButton = self.driver.find_element(By.CSS_SELECTOR,"button[data-sub-type='image']")
        aGoodDetailButton.click()

        #detailed images
        detailImgs = self.driver.find_elements_by_css_selector("img.js-media")

        imgUris = [d.get_attribute('src') for d in detailImgs]
        for i in range(len(imgUris)):
            if(i in [0,3,6,7]):
                good.ImgUriList.append( imgUris[i] )

        #good name
        name = self.driver.find_element(By.CSS_SELECTOR, "#pdp_product_title")
        good.Name = name.get_attribute('innerHTML')
        
        return good

    def GetTodayGoodList(self):
        todayCatch = LoadAttempt.CLoadAttempt()
        try:
            self.driver.get("https://nike.com")
            self.CloseInfoPopups()
            self.OpenGoodsPage()
            wholeGUriList = self.GetGoodsUriList()
            if len(wholeGUriList) > 10:
                for i in range(7):
                    idx = random.randint(0, len(wholeGUriList) -1 )
                    todayCatch.GoodList.append( self.GetDetailedOfGood(wholeGUriList[idx]) )
        except Exception as inst:
            todayCatch.ErrorList.append(inst)
        return todayCatch;





