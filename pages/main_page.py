#-*- coding:utf-8 -*-

from commn.driver import Driver
from pages.update_page import UpdatePage
from pages.jingpin_page import JingpinPage
from pages.fuli_page import FuliPage
from pages.search_page import SearchPage
from commn.base_page import Base
import time

class MainPage(Base):
    """首页"""
    
    #首页4个tab切换页
    update_loc = "tablist-update"
    jingpin_loc = "tablist-supreme"
    fuli_loc = "tablist-gift"
    main = "//*[@text='首页']"
    
    search_loc = "head-login-btn"
    marqueeBar_loc = "marqueeBar"
    @staticmethod
    def go_mainpage():
        """
        启动app,到首页
        :return:MainPage()
        """
        Driver.init()
        return MainPage()
    
    def go_updatepage(self):
        """
        到更新tab页
        :return:
        """
        self.find(self.update_loc).click()
        return UpdatePage()
    
    def go_jingpinpage(self):
        """
        到更新tab页
        :return:
        """
        self.find(self.jingpin_loc).click()
        return JingpinPage()
    
    def go_fulipage(self):
        """
        到更新tab页
        :return:
        """
        self.find(self.fuli_loc).click()
        return FuliPage()
    
    def go_searchepage(self):
        '''
        到搜索页
        :return:SearchPgae()
        '''
        self.find(self.search_loc).click()
        return SearchPage()
    
    def get_marqueeBar(self):
        """
        获取跑马灯数据
        :return: WebElemet List
        """
        return self.find(self.marqueeBar_loc)
        
    
    def get_shouye(self):
        print("================")
        return self.find(self.main)
    
    