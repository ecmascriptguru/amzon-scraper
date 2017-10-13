# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
from config import app_config

import datetime
import time
import os

class UBrowse(object):
    """ Create emulation user browsing """
    def __init__(self):
        ENV = os.getenv('FLASK_CONFIG')
        config = app_config[ENV]
        exec_path = config.CHROME_DRIVER_PATH
        chrome_option = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_option.add_experimental_option("prefs",prefs)

        if ENV != 'dev':
            self.display = Display(visible=0, size=(1200, 900))
            self.display.start()

        self.driver = webdriver.Chrome(executable_path = exec_path, chrome_options=chrome_option)

    def create_screenshot(self, action):
        stime = datetime.datetime.now()
        year = str(stime.year)
        month = str(stime.month)
        day = str(stime.day)
        hour = str(stime.hour)
        minute = str(stime.minute)

        path_error = 'screens/errors/'
        full_path = path_error + "%s.%s.%s-%s-%s_%s.png"%(year, month, day, hour, minute, action)  

        self.driver.save_screenshot(full_path)

    def open_url(self, link):
        self.driver.get(link)

    def close(self):
        if ENV != 'dev':
            self.display.stop()

        self.driver.quit()

    def click_link(self, link, type='xpath'):
        if type == 'by_xpath':
            self.driver.implicitly_wait(5)
            obj = self.driver.find_element_by_xpath(link)
        if type == 'by_class':
            self.driver.implicitly_wait(5)
            obj = self.driver.find_element_by_class_name(link)
        if type == 'by_id':
            self.driver.implicitly_wait(5)
            obj = self.driver.find_element_by_id(link)
        
        if obj:
            obj.click()
        return True

    
if __name__ == "__main__":
    run = UBrowse()
