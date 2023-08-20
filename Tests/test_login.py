# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 04:45:31 2023

@author: hcasl
"""
from selenium import webdriver
import time
import unittest

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import HtmlTestRunner

from Pages.loginPage import LoginPage
from Pages.homePage import HomePage

class TestLogin(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        
        homepage = HomePage(driver)
        homepage.click_dropdown()
        homepage.click_logout()
        
        time.sleep(2)
        
    @classmethod  
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = 'C:/Users/hcasl/.spyder-py3/POMProjectDemo/Reports'))
            


