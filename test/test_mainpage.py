#-*- coding:utf-8 -*-
import pytest
from commn.driver import Driver
from pages.main_page import MainPage

class TestMainPage():
    
    @pytest.fixture(scope="class")
    def driver_setup_teardown(self):
        mainpage = MainPage.go_mainpage()
        yield mainpage
        print("====== teardown ======")
        Driver.get_driver().close_app()
    
    def test_mar(self,driver_setup_teardown):
        """
        验证跑马灯数据显示
        :return:
        """
        re = driver_setup_teardown.get_marqueeBar()
        
        print("111")
        assert re is not None
        
    # def test_aa(self,driver_setup_teardown):
    #     re = driver_setup_teardown.go_searchepage()
    #     print('22222222')
    #     assert re
    
        
    
        