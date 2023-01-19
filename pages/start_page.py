import logging
from time import sleep

from constants.start_page import StartPageConst
from pages.base_page import BasePage


class StartPage(BasePage):
    """Stores methods describes start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.log = logging.getLogger('[StartPage]')

    def sign_in(self, username, password):
        """Sign in using provided values"""

        # Fill fields
        self.fill_fields(xpath=self.const.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_fields(xpath=self.const.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)
        sleep(2)

        # Click on SignIn button
        self.click(xpath=self.const.SIGN_IN_BUTTON_XPATH)
        sleep(2)

    def verify_sign_in_error(self):
        """Verify that text is matched to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_IN_ERROR_XPATH, text=self.const.SIGN_IN_ERROR_TEXT)

    def sign_up(self, username, email, password):
        """Sign up using provided values"""

        # Fill fields
        self.fill_fields(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_fields(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_fields(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        sleep(3)

        # Click SignUp button
        self.click(xpath=self.const.SIGN_UP_BUTTON_XPATH)
        sleep(1)
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)
