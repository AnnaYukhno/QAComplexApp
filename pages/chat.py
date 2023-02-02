import logging
from itertools import zip_longest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants.chat import ChatConsts
from pages.base_page import BasePage


class Chat(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.const = ChatConsts
        self.log = logging.getLogger('[Chat]')

    def send_message(self, text):
        """Send message via chat"""
        self.fill_fields(xpath=self.const.CHAT_FIELD_INPUT_XPATH, value=text + Keys.ENTER)

    def verify_messages_in_chat_window(self, expected_messages):
        """Verify message is displayed in chat window"""
        messages = self.wait_until_displayed_elements(by=By.XPATH, xpath=self.const.SELF_MESSAGES_IN_CHAT_XPATH)
        for message, expected_messages in zip_longest(messages, expected_messages):
            assert message.text.strip() == expected_messages, f'Actual: {message}, Expected: {expected_messages}'
