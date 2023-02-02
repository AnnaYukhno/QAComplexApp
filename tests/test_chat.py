"""Tests related to chat"""
import logging

import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestChat:
    """Stores tests for chat functionality"""

    log = logging.getLogger("[Chat]")

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        return start_page.sign_up(random_user)

    def test_self_messages(self, hello_page):
        """
        Steps:
            - Open chat
            - Send message
            - Verify that message appears
            - Send one more message
            - Verify that both message displayed
        """

        # Open chat
        hello_page.header.navigate_to_the_chat()
        self.log.info('Chat was opened')

        expected_messages = []

        # # Send message
        # message = 'Hello'
        # expected_messages = [message]
        # hello_page.chat.send_message(text=message)
        # self.log.info('The message was sent')
        #
        # # Verify that message appears
        # hello_page.chat.verify_messages_in_chat_window(expected_messages=expected_messages)
        # self.log.info('The message was verified')
        #
        # # Send one more message
        # messages1 = 'My name is John'
        # expected_messages.append(messages1)
        # hello_page.chat.send_message(text=messages1)
        # self.log.info('The second message was sent')
        #
        # # Verify that both message displayed
        # hello_page.chat.verify_messages_in_chat_window(expected_messages)
        # self.log.info('The both messages were verified')

        # Send message
        for i in range(2):
            message = f'Hello{i}'

            # Send message
            expected_messages.append(message)
            hello_page.chat.send_message(text=message)
            self.log.info('The message was sent')

            # Verify that message appears
            hello_page.chat.verify_messages_in_chat_window(expected_messages=expected_messages)
            self.log.info('The message was verified')
