import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains



class Browser:
        browser, service = None, None
        
        
        def __init__(self, driver):
            self.service = Service(driver)

            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory": "/home/gukanaiama/Documentos/Github/YoutubeAutomation/get_voice_script/voices/",
             "directory_upgrade": True}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--headless")

            self.browser = webdriver.Chrome(service=self.service, options = chrome_options)

            
            
        def open_page(self, url):
            self.browser.get(url)
            
        def close_browser(self):
            self.browser.close()

        def reddit_topic(self):
            browser = self.browser
            browser.get('https://ttsmp3.com/text-to-speech/')

            with open("get_voice_script/voice_script.txt", "r") as script_txt:
                buffer_script = script_txt.read()

            time.sleep(2)

            #Create the object for Action Chains
            #actions = ActionChains(browser)

            #insert script in text box
            browser.find_element(By.XPATH, "//textarea[@id='voicetext']").send_keys(buffer_script)

            #selecting option bar
            option_bar = browser.find_element(By.XPATH, "//select[@id='sprachwahl']")
            option_bar.click()
            time.sleep(0.5)
            #Select Ricardo voice
            ricardo_voice = browser.find_element(By.XPATH, "//option[@value='Ricardo']")
            ricardo_voice.click()
            time.sleep(0.5)
            #Download button
            download_buton = browser.find_element(By.XPATH, "//input[@id='downloadenbutton']")
            download_buton.click()
            time.sleep(0.5)



browser = Browser('/snap/bin/chromium.chromedriver')
browser.reddit_topic()
time.sleep(3)
browser.close_browser()