from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BasePage import BasePage


class BuyProductPage(BasePage):
    '''locators'''
    BUY_BUTTON = (By.ID,"buy-now-button")

    def __init__(self, driver):
        self.driver = driver

    def click_buy_button(self):
        return self.driver.find_element(*BuyProductPage.BUY_BUTTON)

