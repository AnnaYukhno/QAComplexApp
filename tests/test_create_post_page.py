"""Tests realsted to create post page"""
import logging

import pytest

from constants.base import BaseConstants
from constants.create_post_page import CreatePostPageConsts
from pages import utils


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestCreatePostPage:
    """Stores tests for create post page base functionality"""

    log = logging.getLogger("[CreatePostPage]")

    @pytest.mark.parametrize("unique", [True, False])
    @pytest.mark.parametrize("privacy", [CreatePostPageConsts.PUBLIC_PRIVACY, CreatePostPageConsts.PRIVATE_PRIVACY,
                                         CreatePostPageConsts.GROUP_PRIVACY])
    def test_create_post_with_settings(self, start_page, unique, privacy):
        """
        - Steps:
            - Sign Up as a user
            - Navigate to create post page
            - Create post by provided title, body, unique and privacy
            - Verify that post was created successfully
        """
        # Sign Up as a user
        username = utils.random_text(length=3)
        password = utils.random_text(length=6)
        hello_page = start_page.sign_up(username=username, email=f'{username}@gmail.com', password=password)
        self.log.info('Signed up with valid credentials')

        # Navigate to create post page
        create_post_page = hello_page.navigate_to_create_post()
        self.log.info('Navigated to create post page')

        # Create post by provided title, body, unique and privacy
        post_page = create_post_page.create_post(unique_post=unique, post_privacy=privacy)
        self.log.info('Post was created')

        # Verify that post was created successfully
        post_page.verify_created_post(unique_post=unique, post_privacy=privacy)
