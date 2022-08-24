from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class LoginPage(BasePage):
    '''locators for email and password'''
    EMAIL = (By.ID,"ap_email")
    EMAIL_CONTINUE = (By.ID,"continue")
    PASSWORD = (By.ID,"ap_password")
    PASSWORD_CONTINUE = (By.ID,"signInSubmit")
    ERROR = (By.XPATH,"//span[@class='a-list-item']")

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self):
        return self.driver.find_element(*LoginPage.EMAIL)

    def click_email_continue(self):
        return self.driver.find_element(*LoginPage.EMAIL_CONTINUE)

    def enter_password(self):
        return self.driver.find_element(*LoginPage.PASSWORD)

    def click_password_continue(self):
        return self.driver.find_element(*LoginPage.PASSWORD_CONTINUE)

    def error(self):
        return self.driver.find_element(*LoginPage.ERROR)
