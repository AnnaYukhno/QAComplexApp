import logging

from constants.my_profile_page import MyProfilePageConsts
from pages.base_page import BasePage
from pages.header import Header


class MyProfilePage(BasePage):
    """Stores methods describes my profile page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = MyProfilePageConsts
        self.header = Header(self.driver)
        self.log = logging.getLogger('[MyProfilePage]')

    def verify_username_at_my_profile_page(self, username):
        """Verify that username meets validate username"""
        assert self.compare_element_text(xpath=self.const.MY_PROFILE_USERNAME_XPATH, text=username.lower(),
                                         strip=True)
