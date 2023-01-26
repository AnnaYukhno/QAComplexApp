import logging

from constants.header import HeaderConsts
from pages.base_page import BasePage


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.const = HeaderConsts
        self.log = logging.getLogger('[Header]')

    def sign_in(self, username, password):
        """Sign in using provided values"""

        # Fill fields
        self.fill_fields(xpath=self.const.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_fields(xpath=self.const.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)

        # Click on SignIn button
        self.click(xpath=self.const.SIGN_IN_BUTTON_XPATH)
