import logging
from time import sleep

from constants.hello_page import HelloPageConst
from pages.base_page import BasePage


class HelloPage(BasePage):
    """Stores methods describes hello page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = HelloPageConst
        self.log = logging.getLogger('[HelloPage]')

    def verify_sign_up_message(self, username):
        """Verify sign up message"""
        assert self.compare_element_text(xpath=self.const.SIGN_OUT_BUTTON_XPATH, text=self.const.SIGN_OUT_BUTTON_TEXT)
        assert self.compare_element_text(
            xpath=self.const.HELLO_PAGE_MESSAGE_XPATH, text=f'Hello {username.lower()}, your feed is empty.'
        )
        sleep(2)
