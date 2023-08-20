# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 09:15:36 2023

@author: hcasl
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.locators import Locators

class HomePage():
    
    def __init__(self,driver):
        self.driver = driver
        
        self.dropdown_class_name = Locators.dropdown_class_name
        self.logout_button_link_text = Locators.logout_button_link_text
        
    def click_dropdown(self):
        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, self.dropdown_class_name))
                )
            dropdown.click()
        except:
            self.driver.quit()

        
    def click_logout(self):
        try:
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, self.logout_button_link_text))
                )
            logout_button.click()
        except:
            self.driver.quit()
        
