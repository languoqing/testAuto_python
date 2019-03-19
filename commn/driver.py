#-*- coding:utf-8 -*-
from appium import webdriver


class Driver:
    driver = None
    
    @staticmethod
    def init():
        '''初始化'''
        caps = {}
        caps["platformName"] = "ANDROID"
        caps["platformVersion"] = "8.1.0"
        caps["deviceName"] = "vivo Y85A"
        caps["app"] = "com.pingan.gamehall"
        caps["noReset"] = True
        caps["udid"] = "7bff6865"
        caps["appActivity"] = ".MainActivity"
        caps["clearSystemFiles"] = True
        Driver.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        Driver.driver.implicitly_wait(3)
        
        
    
    @staticmethod
    def get_driver():
        return Driver.driver