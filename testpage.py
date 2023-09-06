import logging
import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    dict = {}
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        dict[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        dict[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):

        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=10)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        text = field.text

        return text

# ENTER
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.dict["LOCATOR_LOGIN_FIELD"], word, description="username")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.dict["LOCATOR_PASS_FIELD"], word, description="password")

    def new_title(self, word):
        self.enter_text_into_field(TestSearchLocators.dict["LOCATOR_POST_TITLE"], word, description="title")

    def new_description(self, word):
        self.enter_text_into_field(TestSearchLocators.dict["LOCATOR_POST_DESCRIPTION"], word, description="description")

    def new_content(self, word):
        self.enter_text_into_field(TestSearchLocators.dict["LOCATOR_POST_CONTENT"], word, description="content")

    def your_name(self, word):
        self.enter_text_into_field(TestSearchLocators.dict["LOCATOR_CONTACT_NAME_FIELD"], word, description="username")

    def your_email(self, word):
        self.enter_text_into_field(TestSearchLocators.dict["LOCATOR_CONTACT_EMAIL_FIELD"], word, description="email")

    def message(self, word):
        self.enter_text_into_field(TestSearchLocators.dict["LOCATOR_CONTACT_CONTENT_FIELD"], word,
                                   description="message")

    # CLICK

    def click_login_button(self):
        self.click_button(TestSearchLocators.dict["LOCATOR_LOGIN_BTN"], description="login")

    def new_post_btn(self):
        self.click_button(TestSearchLocators.dict["LOCATOR_NEW_POST_BTN"], description="new post")

    def post_save_button(self):
        self.click_button(TestSearchLocators.dict["LOCATOR_SAVE_BTN"], description="save post")

    def new_contact_btn(self):
        self.click_button(TestSearchLocators.dict["LOCATOR_CONTACT_BTN"], description="contact")

    def contact_us_btn(self):
        self.click_button(TestSearchLocators.dict["LOCATOR_CONTACT_SAVE_BTN"], description="contact save")

    # GET TEXT

    def expected_title(self):
        return self.get_text_from_element(TestSearchLocators.dict["LOCATOR_TITLE_TEXT"], description="title")

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.dict["LOCATOR_ERROR_FIELD"], description="error label")

    def get_login_text(self):
        return self.get_text_from_element(TestSearchLocators.dict["LOCATOR_HELLO_LOGIN"], description="user profile name")

    def alert(self):
        logging.info("Get alert text")
        alert_t = self.alert_text()
        logging.info(f"{alert_t}")
        return alert_t
