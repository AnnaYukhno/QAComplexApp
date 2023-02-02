import logging

from constants.start_page import StartPageConst
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import wait_until_ok


class StartPage(BasePage):
    """Stores methods describes start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.header = Header(self.driver)
        self.log = logging.getLogger('[StartPage]')

    def verify_sign_in_error(self):
        """Verify that text is matched to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_IN_ERROR_XPATH, text=self.const.SIGN_IN_ERROR_TEXT)

    @wait_until_ok(timeout=3, period=0.5)
    def click_and_validate_sign_up_button(self):
        """Click Sign up button until it disappear"""
        self.click(self.const.SIGN_UP_BUTTON_XPATH)
        assert not self.is_element_exists(self.const.SIGN_UP_BUTTON_XPATH)

    def sign_up(self, user, verify=True):
        """Sign up using provided values"""

        # Fill fields
        self.fill_fields(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_fields(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_fields(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)

        # Click SignUp button
        if verify:
            self.click_and_validate_sign_up_button()
            from pages.hello_page import HelloPage
            return HelloPage(self.driver)
        else:
            self.click(self.const.SIGN_UP_BUTTON_XPATH)

    def verify_sign_in_exists(self):
        """Verify that SignIn button is present on the page"""
        assert self.is_element_exists(xpath=self.header.const.SIGN_IN_BUTTON_XPATH)
