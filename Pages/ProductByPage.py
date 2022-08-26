from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class BuyProductPage(BasePage):
    '''locators'''
    PRODUCT_TITLE = (By.ID, "productTitle")
    BUY_BUTTON = (By.ID,"buy-now-button")

    def __init__(self, driver):
        self.driver = driver

    def product_title(self):
        #self.wait_clickable(BuyProductPage.BUY_BUTTON)
        return self.driver.find_element(*BuyProductPage.PRODUCT_TITLE)

    def click_buy_button(self):
        #self.wait_clickable(BuyProductPage.BUY_BUTTON)
        #name = self.driver.find_element(*BuyProductPage.PRODUCT_TITLE).text
        #if 'Apple' in name:
            #self.waiting_until_item_enabled(BuyProductPage.BUY_BUTTON)
         return self.driver.find_element(*BuyProductPage.BUY_BUTTON)
        #else:
             #print("out of stock")

