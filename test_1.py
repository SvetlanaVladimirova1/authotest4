import logging
import time
from conftest import testdata
from testpage import OperationsHelper


def test_step1(browser):
    logging.info('Test1 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401', 'test1 failed'


def test_step2(browser):
    logging.info('Test2 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_login_text() == f'Hello, {testdata["username"]}', 'test2 failed'


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.new_post_btn()
    testpage.new_title(testdata['title'])
    testpage.new_description(testdata['description'])
    testpage.new_content(testdata['content'])
    testpage.post_save_button()
    time.sleep(testdata['sleep_time'])
    assert testpage.expected_title() == f'{testdata["title"]}'


def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationsHelper(browser)
    testpage.new_contact_btn()
    testpage.your_name(testdata['username'])
    testpage.your_email(testdata['email'])
    testpage.message(testdata['message'])
    testpage.contact_us_btn()
    time.sleep(testdata['sleep_time'])
    assert testpage.alert() == testdata['alert_text']
