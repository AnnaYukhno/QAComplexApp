import logging

from constants.create_post_page import CreatePostPageConsts
from pages import utils
from pages.base_page import BasePage
from pages.header import Header


class CreatePostPage(BasePage):
    """Stores methods describes create post page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = CreatePostPageConsts
        self.header = Header(self.driver)
        self.log = logging.getLogger('[CreatePostPage]')

    def create_post(self, unique_post, post_privacy):
        """Create post using provided value"""
        # Fill fields
        self.fill_fields(xpath=self.const.TITLE_INPUT_XPATH, value=utils.random_post(5))
        self.fill_fields(xpath=self.const.BODY_TEXTAREA_XPATH, value=utils.random_post(50))

        # Choose UniquePost checkbox
        if unique_post:
            self.click(self.const.UNIQUE_POST_CHECKBOX_XPATH)
        else:
            assert not self.driver.find_element('xpath', self.const.UNIQUE_POST_CHECKBOX_XPATH).is_selected()

        # Choose SelectValue down-menu
        if post_privacy == self.const.PUBLIC_PRIVACY:
            self.click(self.const.PUBLIC_POST_OPTION_XPATH)
        elif post_privacy == self.const.PRIVATE_PRIVACY:
            self.click(self.const.PRIVATE_POST_OPTION_XPATH)
        elif post_privacy == self.const.GROUP_PRIVACY:
            self.click(self.const.GROUP_POST_OPTION_XPATH)
        else:
            self.click(self.const.PUBLIC_POST_OPTION_XPATH)

        # Click Save Post button
        self.click(xpath=self.const.SAVE_NEW_POST_BUTTON_XPATH)

        from pages.post_page import PostPage
        return PostPage(self.driver)
