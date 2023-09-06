import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser_t = testdata['browser']
    username = testdata['username']
    password = testdata['password']
    alert = testdata['alert_text']
    api_address = testdata['address_log_API']

S = requests.Session()


@pytest.fixture(scope='session')
def browser():
    if browser_t == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(testdata['implicitly_wait'])
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def api_token():
    token = S.post(url=api_address, data={'username': username, 'password': password})
    return token.json()['token']
