import logging

from selenium.webdriver.common.by import By

from constants.post_page import PostPageConsts
from pages.base_page import BasePage
from pages.header import Header


class PostPage(BasePage):
    """Stores methods describes post page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = PostPageConsts
        self.header = Header(self.driver)
        self.log = logging.getLogger('[PostPage]')

    def verify_created_post(self, unique_post, post_privacy):
        """Verify post creation message"""
        assert self.compare_element_text(xpath=self.const.POST_CREATED_MESSAGE_XPATH,
                                         text=self.const.POST_CREATED_MESSAGE_TEXT)
        self.wait_until_displayed(By.XPATH, self.const.POST_SETTINGS_MESSAGE_XPATH)

        if unique_post:
            assert self.const.UNIQUE_POST_TEXT in self.driver.page_source
        else:
            assert self.const.NON_UNIQUE_POST_TEXT in self.driver.page_source

        assert self.compare_element_text(xpath=self.const.PRIVACY_MESSAGE_XPATH, text=post_privacy)
