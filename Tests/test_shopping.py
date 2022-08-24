import time
import traceback
from logging import exception

from py import log
from selenium.common import NoSuchElementException

from Config.confiq import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductByPage import BuyProductPage
from utilities.BasePage import BasePage


class Test_Shopping(BasePage):

    def test_verify_homePage(self):
        self.driver.implicitly_wait(10)
        '''verifying home page title'''
        title = self.driver.title
        assert title == TestData.HOME_PAGE_TITLE
        self.message_logging("successfully verified home page title")

    '''to search Product'''
    def test_searchProduct(self, params):
        hp_obj = HomePage(self.driver)
        '''searching product name iphone and adding explicit wait'''
        self.wait_presence(hp_obj.PRODUCT_NAME)
        hp_obj.enter_product_name(params)
        self.message_logging("succefully searched the iphone ")

        '''to get total results'''
        iphones = hp_obj.get_list_of_iphones()
        no_phones = len(iphones)
        print("total number of iphones in list:", no_phones)

        '''to print results title'''
        for phone in iphones:
            self.message_logging(phone.text)
        self.message_logging("printed all results product title ")

    def test_select_fourthProduct(self):
        hp_obj = HomePage(self.driver)
        '''to select fourt product and click on it  '''
        hp_obj.click_fourthProduct()
        self.message_logging("succesfully clicked on fourth product")

    def test_buy_iphone(self):
        bp_obj = BuyProductPage(self.driver)
        '''to go parnet window to child window'''
        bp_obj.window_handles()

        '''wait until button is enabled'''
        self.waiting_until_item_enabled(bp_obj.click_buy_button())
        '''click on buy button'''
        bp_obj.click_buy_button().click()
        self.message_logging("clicked on the buy button")

    def test_login(self, params):
        lg_obj = LoginPage(self.driver)
        '''to enetr user name through terminal'''
        lg_obj.enter_email().send_keys(params['username'])

        '''wait until continue button is enabled'''
        self.waiting_until_item_enabled(lg_obj.click_email_continue())
        '''to click on continue button'''
        lg_obj.click_email_continue().click()
        self.message_logging("succesfully clicked the continue button")

        '''to enter wrong password through terminal'''
        lg_obj.enter_password().send_keys(params['password'])

        '''to click on continue button'''
        self.waiting_until_item_enabled(lg_obj.click_password_continue())
        lg_obj.click_password_continue().click()
        self.message_logging("succesfully clciked the continue button")

        '''to verify error message'''
        try:
            error_msg = lg_obj.error().text
            if TestData.VERIFY_ERROR_MSG1 in error_msg:
                self.message_logging(TestData.VERIFY_ERROR_MSG1)
            elif TestData.VERIFY_ERROR_MSG2 in error_msg :
                self.message_logging(TestData.VERIFY_ERROR_MSG1)

        except AssertionError:
            print(traceback.format_exc())







