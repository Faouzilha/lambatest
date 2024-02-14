# -*- coding: utf-8 -*-
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import unittest
import os

class TestLoginLogout(unittest.TestCase):

    def setUp(self):

        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        # self.base_url = "https://www.google.com/"
        # self.verificationErrors = []
        # self.accept_next_alert = True

        lt_options = {
            "user": "hfaouzilha",
            "accessKey": "VeBWBrxknTEKnh5W5Vrs3uG1I300OJQxUiDx41prU5iAgX1PHP",
            "build": "UnitTest-Selenium-Sample",
            "name": "UnitTest-Selenium-Test",
            "platformName": "Windows 11",
            "w3c": True,
            "browserName": "Chrome",
            "browserVersion": "latest",
            "selenium_version": "4.8.0"
        }
        
        browser_options = ChromeOptions()
        browser_options.set_capability('LT:Options', lt_options)

        self.driver = webdriver.Remote(
            command_executor="http://hub.lambdatest.com:80/wd/hub",
            options=browser_options)


    # Fonction pour le processus de connexion
    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
    
    # Fonction pour le processus de déconnexion
    def logout(self, driver):
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.find_element(By.ID, "logout_sidebar_link").click()
        driver.implicitly_wait(10)
    
    def test_example(self):
        driver = self.driver

        # Partie 1 - Login
        self.login("standard_user", "secret_sauce")

        # Partie 2 - Ajout Panier
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']/a").click()

        elements_du_panier = driver.find_elements(By.XPATH, "//div[@id='cart_contents_container']/div/div/div[@class='cart_item']")
        assert len(elements_du_panier) == 3, "Le nombre d'éléments dans le panier n'est pas égal à 3"

        # Partie 3 - Modification Panier
        driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()

        elements_du_panier = driver.find_elements(By.XPATH, "//div[@id='cart_contents_container']/div/div/div[@class='cart_item']")
        assert len(elements_du_panier) == 2, "Le nombre d'éléments dans le panier n'est pas égal à 2"

        # Partie 4 - Validation du panier

        # ...    

        # Partie 5 - Logout
        self.logout(driver)
       
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
