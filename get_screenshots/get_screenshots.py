import numpy as np
import cv2
import pyautogui
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from PIL import Image

from io import BytesIO


class Browser:
    browser, service = None, None
    
    
    def __init__(self, driver):
        
        #Tira o pop-up inicial do chrome
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service, options=chrome_options)
        
    def open_page(self, url):
        self.browser.get(url)
        
    def close_browser(self):
        self.browser.close()
        
    def reddit_topic(self):
        
        browser = self.browser
        
        browser.get('https://www.reddit.com/r/RelatosDoReddit/comments/zynl95/fale_um_poder_in%C3%BAtil_e_a_outra_pessoa_vai_deixar/')
        
        time.sleep(4)
        
        resp = browser.find_elements(By.XPATH, '//p')
        
        for x in range(3):
            print("entrouaqui")
            time.sleep(2)
            
            location = resp[x].location
            size = resp[x].size
            
            print(location)
            print(size)
            
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            
            png = browser.get_screenshot_as_png()
            im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

            if x != 0: top = (x)*(top-250)

            im = im.crop((left, top, right, bottom)) # crop points
            im.save(f'get_screenshots/images/teste_ultimoclan{x}.png') # saves new cropped image
            
            if x != 2 :
                browser.execute_script("window.scrollBy(0, 250)","")
                
                
            
            

screen_size = pyautogui.size()            


browser = Browser('/snap/bin/chromium.chromedriver')
browser.reddit_topic()
time.sleep(3)
browser.close_browser()


