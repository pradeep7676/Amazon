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
        self.wait_presence(LoginPage.EMAIL)
        return self.driver.find_element(*LoginPage.EMAIL)

    def click_email_continue(self):
        self.wait_clickable(LoginPage.EMAIL_CONTINUE)
        return self.driver.find_element(*LoginPage.EMAIL_CONTINUE)

    def enter_password(self):
        self.wait_presence(LoginPage.PASSWORD)
        return self.driver.find_element(*LoginPage.PASSWORD)

    def click_password_continue(self):
        self.wait_clickable(LoginPage.PASSWORD_CONTINUE)
        return self.driver.find_element(*LoginPage.PASSWORD_CONTINUE)

    def error(self):
        return self.driver.find_element(*LoginPage.ERROR)
