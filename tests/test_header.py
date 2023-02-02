"""Tests related to start page"""
import logging

import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestHeader:
    log = logging.getLogger('[Header]')

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        return start_page.sign_up(random_user)

    def test_sign_out_at_header(self, hello_page):
        """
            Steps:
            - Click on Sign Out Button
            - Verify the result
        """
        # Click on Sign Out Button
        start_page = hello_page.header.sign_out()
        self.log.info('Signed out')

        # Verify the result
        start_page.verify_sign_in_exists()
        self.log.info('Signed out')

    def test_my_profile_page(self, hello_page, random_user):
        """
            Steps:
            - Click on "My Profile"
            - Verify profile username
        """
        # Click on "My Profile"
        my_profile_page = hello_page.navigate_to_my_profile_page(random_user.username)
        self.log.info('Navigated to My Profile Page')

        # Verify profile username
        my_profile_page.verify_username_at_my_profile_page(random_user.username)
        self.log.info('My profile username is verified')
