import logging

from constants.hello_page import HelloPageConst
from pages.base_page import BasePage
from pages.chat import Chat
from pages.header import Header


class HelloPage(BasePage):
    """Stores methods describes hello page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = HelloPageConst
        self.header = Header(self.driver)
        self.chat = Chat(self.driver)
        self.log = logging.getLogger('[HelloPage]')

    def verify_sign_up_message(self, username):
        """Verify sign up message"""

        assert self.compare_element_text(xpath=self.header.const.SIGN_OUT_BUTTON_XPATH,
                                         text=self.header.const.SIGN_OUT_BUTTON_TEXT)
        assert self.compare_element_text(
            xpath=self.const.HELLO_PAGE_MESSAGE_XPATH, text=f'Hello {username.lower()}, your feed is empty.'
        )

    def navigate_to_create_post(self):
        """Navigate to create post page via header button"""
        self.click(xpath=self.header.const.CREATE_POST_BUTTON_XPATH)

        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    def navigate_to_my_profile_page(self, username):
        """Navigate to my profile page via header button"""
        self.click(xpath=self.header.const.MY_PROFILE_BUTTON_XPATH.format(username=username.lower()))

        from pages.my_profile_page import MyProfilePage
        return MyProfilePage(self.driver)
