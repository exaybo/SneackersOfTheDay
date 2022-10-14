from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import LoadAttempt
import traceback
import time


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
            #otherWidows = self.driver.find_elements_by_css_selector("[data-var='closeButton']")
            otherWidows = self.driver.find_elements(By.CSS_SELECTOR, "[data-var='closeButton']")
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
        for i in range(random.randint(3,7)):
            actions = webdriver.ActionChains(self.driver)
            actions.send_keys('\ue010')
            actions.perform()
            time.sleep(5)

        #Goods
        goodLinks = self.driver.find_elements(By.CSS_SELECTOR,"div[data-product-position] a[aria-label]")

        #Goods uris
        goodUris = [g.get_attribute('href') for g in goodLinks]
        return goodUris

    def GetDetailedOfGood(self, uri, images):
        good = LoadAttempt.CGood()
        good["Uri"] = uri
        good["Date"] = datetime.utcnow()
        #navigate to random good
        #driver.get(goodUris[random.randint(0,len(goodUris))])
        self.driver.get(uri)

        #show good detailed images
        time.sleep(5)
        aGoodDetailButton = self.driver.find_element(By.CSS_SELECTOR,"button[data-sub-type='image']")
        aGoodDetailButton.click()

        #detailed images
        detailImgs = self.driver.find_elements(By.CSS_SELECTOR,"img.js-media")

        imgUris = [d.get_attribute('src') for d in detailImgs]
        for i in range(len(imgUris)):
            if(i in [0,3,6,7]):
                good["ImgUriList"].append( imgUris[i] )

        #good name
        name = self.driver.find_element(By.CSS_SELECTOR, "#pdp_product_title")
        good["Name"] = name.get_attribute('innerHTML')
        
        #load bin images
        for iu in good["ImgUriList"]:
            bi = LoadAttempt.CBinImage()
            bi.loadBinImage(iu)
            images.append(bi)

        return good

    

    def GetTodayGoodList(self, attempt, sneackers, images):        
        try:
            self.driver.implicitly_wait(10)
            self.driver.get("https://nike.com")
            self.CloseInfoPopups()
            self.OpenGoodsPage()
            wholeGUriList = self.GetGoodsUriList()
            attempt["CountOfLoaded"] = 0
            grabCount = min(len(wholeGUriList), attempt["CountToLoad"])
            if grabCount:
                for i in range(grabCount):
                    try:
                        idx = random.randint(0, len(wholeGUriList) -1 )
                        sneackers.append( self.GetDetailedOfGood(wholeGUriList[idx], images) )
                        attempt["CountOfLoaded"] += 1
                    except Exception:
                        msg = traceback.format_exc()
                        attempt["ErrorList"].append(msg)
        except Exception:
            msg = traceback.format_exc()
            attempt["ErrorList"].append(msg)
