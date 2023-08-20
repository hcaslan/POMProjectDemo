# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 09:07:56 2023

@author: hcasl
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.locators import Locators

class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath
        
    def enter_username(self, username):
        
        try:
            username_textbox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, self.username_textbox_name))
                )
            username_textbox.clear()
            username_textbox.send_keys("Admin")
        except:
            self.driver.quit()
                       
    def enter_password(self, password):

        try:
            password_textbox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, self.password_textbox_name))
                )
            password_textbox.clear()
            password_textbox.send_keys("admin123")
        except:
            self.driver.quit()
        
    def click_login(self):
        
        try:
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.login_button_xpath))
                )
            login_button.click()
        except:
            self.driver.quit()
