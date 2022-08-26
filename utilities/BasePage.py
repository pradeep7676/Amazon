import inspect
import logging
import time


import pytest
from py import log
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup", "params")
class BasePage:
    def wait_presence(self, path):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(path))

    def wait_clickable(self, path):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(path))

    '''to switch child window'''
    def child_window_handles(self):
        child = self.driver.window_handles
        self.driver.switch_to.window(child[1])

    def Parent_window_handles(self):
        child = self.driver.window_handles
        self.driver.switch_to.window(child[0])

    '''to print logging messages'''

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    '''to wait until any item enabled'''
    def waiting_until_item_enabled(self, item, time_out=30, interval_unit=0.5):
        log = self.getLogger()
        end_time = time.time() + time_out
        #log.info(f"{item} : is Waiting for Enable")
        while time.time() < end_time and not item.is_enabled():
            time.sleep(interval_unit)

        if time.time() > end_time:
            log.info(f"{item} : is not enable error")
            raise TimeoutError()