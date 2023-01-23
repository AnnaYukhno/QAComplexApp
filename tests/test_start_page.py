"""Tests related to start page"""
import logging

from pages import utils


class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[StartPage]")

    def test_start_page(self, start_page):
        """
        - Steps:
            - Login as invalid user
            - Verify error
        """

        # Login as invalid user
        start_page.sign_in(username="test123", password="pwd123")
        self.log.info('Logged in as invalid user')

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info('Error was verified')

    def test_registration(self, start_page):
        """
        -Step:
            - Prepare test data
            - Sign up with valid credentials
            - Verify registration
        """
        # Prepare test data
        username = utils.random_text(length=3)
        password = utils.random_text(length=6)

        # Sign up with valid credentials
        hello_page = start_page.sign_up(username=username, email=f'{username}@gmail.com', password=password)
        self.log.info('Signed up with valid credentials')

        # Verify registration
        hello_page.verify_sign_up_message(username=username)
        self.log.info('Registration was verified')

    def test_invalid_username(self, start_page, verify=False):
        """
        - Steps:
            - Prepare test data
            - Fill invalid username
            - Verify the error message
        """
        # Prepare data for username
        username = utils.random_text(length=1)

        # Fill invalid username
        start_page.sign_up(username=username, email="", password="", verify=False)
        self.log.info('Username was filled')

        # Verify the error message
        assert 'Username must be at least 3 characters.' in start_page.driver.page_source
        self.log.info("Invalid username was verified")

    def test_valid_username(self, start_page):
        """
        - Steps:
            - Prepare test data
            - Fill valid username
            - Verify the error message isn't displayed
        """
        # Prepare data for username
        username = utils.random_text(length=2)

        # Fill invalid username
        start_page.sign_up(username=username, email="", password="", verify=False)
        self.log.info('Username was filled')

        # Verify the error message
        assert not 'Username must be at least 3 characters.' in start_page.driver.page_source
        self.log.info("Valid username was verified")

    def test_empty_credentials(self, start_page):
        """
        - Steps:
            - Prepare test data
            - Fill username and leave email, password empty
            - Verify error messages
        """

        # Prepare test data
        username = utils.random_text(length=2)

        # Fill username and leave email, password empty
        start_page.sign_up(username=username, email="", password="", verify=False)
        self.log.info('Filled username and left email, password empty')

        # Verify error messages
        assert 'You must provide a valid email address.' in start_page.driver.page_source
        assert 'Password must be at least 12 characters.' in start_page.driver.page_source
        self.log.info("Invalid email, password were verified")
