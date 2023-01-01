import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Browser:
    browser, service = None, None
    
    
    def __init__(self, driver):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)
        
    def open_page(self, url):
        self.browser.get(url)
        
    def close_browser(self):
        self.browser.close()
        
    def reddit_topic(self):
        browser = self.browser
        browser.get('https://www.reddit.com/r/RelatosDoReddit/comments/zynl95/fale_um_poder_in%C3%BAtil_e_a_outra_pessoa_vai_deixar/')
        resp = browser.find_elements(By.XPATH, '//p')
        
        for x in range(len(resp)):
            print(resp[x].text)
            
        list_resturn = list()
        return [resp[0], resp[1], resp[2]]

browser = Browser('/snap/bin/chromium.chromedriver')
browser.reddit_topic()
time.sleep(3)
browser.close_browser()