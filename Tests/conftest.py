from webbrowser import Chrome

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Config.confiq import TestData

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption("--username", action="store", help="input username")
    parser.addoption("--password", action="store", help="input password")
    parser.addoption("--productName", action="store", help="input productName")

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    if browser_name == "chrome":
        s = Service(TestData.chrome_executablepath)
        driver = webdriver.Chrome(service=s, options=chrome_options)
    elif browser_name == "firefox":
        s = Service(TestData.fireFox_executablepath)
        driver = webdriver.Firefox(service=s)

    driver.get(TestData.baseUrl)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture
def params(request):
    params = {}
    params['username'] = request.config.getoption('--username')
    params['password'] = request.config.getoption('--password')
    params['productName'] = request.config.getoption('--productName')
    if params['username'] is None and params['password'] is None:
        pytest.skip()
    return params

