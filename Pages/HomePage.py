
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities.BasePage import BasePage


class HomePage(BasePage):
    '''locators'''
    PRODUCT_NAME = (By.ID, "twotabsearchtextbox")
    LIST_OF_IPHONES = (By.XPATH,"//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
    FOURTH_PRODUCT = (By.XPATH, "(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[4]")
    FIFTH_PRODUCT = (By.XPATH,"(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[5]")
    def __init__(self, driver):
        self.driver = driver

    '''To enter in text box '''
    def enter_product_name(self, params):
        log = self.getLogger()
        if self.searchBox_is_present():
            self.wait_presence(HomePage.PRODUCT_NAME)
            self.driver.find_element(*HomePage.PRODUCT_NAME).send_keys(params['productName'])
            log.info("search box is present")
            self.driver.find_element(*HomePage.PRODUCT_NAME).send_keys(Keys.ENTER)
        else:
            log.info("search box is not present")

    '''to check search box is enabled or not '''
    def searchBox_is_present(self):
        search_box = self.driver.find_elements(*HomePage.PRODUCT_NAME)
        searchBox = False
        if len(search_box) >= 1:
            searchBox = True
        return searchBox

    '''to get list of phones'''
    def get_list_of_iphones(self):
        self.wait_presence(HomePage.LIST_OF_IPHONES)
        return self.driver.find_elements(*HomePage.LIST_OF_IPHONES)

    '''to click on fourth product'''
    def click_fourthProduct(self):
        self.wait_presence(HomePage.FOURTH_PRODUCT)
        return self.driver.find_element(*HomePage.FOURTH_PRODUCT).click()

    def click_fifthProduct(self):
        self.wait_presence(HomePage.FOURTH_PRODUCT)
        return self.driver.find_element(*HomePage.FIFTH_PRODUCT).click()

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,700);")








