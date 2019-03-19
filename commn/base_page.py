#-*- coding:utf-8 -*-
from commn.driver import Driver
from appium.webdriver.common.mobileby import By
import re

class Base:
    
    
    def find(self,element_loc):
        """
        参数是一个定位元素，使用在Xpath和ID定位，Xpath用于//*开头
        :param element_loc:
        :return: WebElemet
        """
        re = None
        if element_loc.startswith("//*"):
            try:
                re = Driver.get_driver().find_element(By.XPATH,element_loc)
            except Exception as e:
                print("{}查找有问题：{}".format(element_loc,e))
        else:
            try:
                re = Driver.get_driver().find_element(By.ID,element_loc)
            except Exception as e:
                print("{} 查找有问题：{}".format(element_loc,e))
        return re
        
    
    
        