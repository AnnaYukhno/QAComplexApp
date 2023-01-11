"""Tests related to start page"""
import logging
import random
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generate random number"""
        return random.choice(string.digits)

    @staticmethod
    def random_str():
        """Generate random string"""
        return random.choice(string.ascii_letters)

    def test_start_page(self):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login
            - Fill password
            - Click on SignIn button
            - Verify error
        """
        # Open start page
        driver = webdriver.Chrome(executable_path="C:\Development\QAComplexApp\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # Fill login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys("test123")
        self.log.info("Login field was filled")
        sleep(1)

        # Fill password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password_field.clear()
        password_field.send_keys("pwd123")
        self.log.info("Password field was filled")
        sleep(1)

        # Click on SignIn button
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sign_in_button.click()
        self.log.info("SignUp button was click")
        sleep(1)

        # Verify error
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Error"
        self.log.info("Error message was verified")
        sleep(1)

        driver.close()

    def test_registration(self):
        """
        - Pre-conditions:
            - Open start page
        -Step:
            - Fill username
            - Fill email
            - Fill password
            - Click SignUp button
            - Verify registration
        """

        # Open start page
        driver = webdriver.Chrome(executable_path="C:\Development\QAComplexApp\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info('Start page was opened')

        # Fill username
        username_rg_field = driver.find_element(by=By.XPATH, value='.//input[@id="username-register"]')
        username_rg_field.clear()

        length_username_rg = 3
        username_rg = ''
        for i in range(length_username_rg):
            username_rg += ''.join(self.random_str() + self.random_num())
        username_rg_field.send_keys(username_rg)
        self.log.info('Username was filled')

        # Fill email
        email_rg_field = driver.find_element(by=By.XPATH, value='.//input[@id="email-register"]')
        email_rg_field.clear()
        email_rg_field.send_keys(username_rg + '@gmail.com')
        self.log.info('Email for registration was filled')
        sleep(2)

        # Fill password
        password_rg_field = driver.find_element(by=By.XPATH, value='.//input[@id="password-register"]')
        password_rg_field.clear()
        password_rg_length = 6
        password_rg = ''
        for i in range(password_rg_length):
            password_rg += ''.join(self.random_str() + self.random_num())
        password_rg_field.send_keys(password_rg)
        self.log.info('Password for registration was filled')
        sleep(2)

        # Click on SignUp button
        driver.find_element(by=By.XPATH, value=".//button[@type='submit']").click()
        self.log.info("SignUp button was click")

        # Verify registration
        sign_out = driver.find_element(by=By.XPATH, value='.//button[@class="btn btn-sm btn-secondary"]')
        hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        assert sign_out.text == 'Sign Out'
        assert hello_message.text == f"Hello {username_rg.lower()}, your feed is empty."
        self.log.info('Registration was verified')
        sleep(2)

        driver.close()

    def test_invalid_username(self):
        """
        - Pre-condition:
            Open start page
        - Steps:
            Fill invalid username
            Verify the error message
        """

        # Open start page
        driver = webdriver.Chrome(executable_path="C:\Development\QAComplexApp\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info('Start page was opened')

        # Fill invalid username
        username_rg_field = driver.find_element(by=By.XPATH, value='.//input[@id="username-register"]')
        username_rg_field.clear()

        length_username_rg = 1
        username_rg = ''
        for i in range(length_username_rg):
            username_rg += ''.join(self.random_str() + self.random_num())
        username_rg_field.send_keys(username_rg)
        self.log.info('Username was filled')
        sleep(2)

        # Verify the error message
        assert 'Username must be at least 3 characters.' in driver.page_source
        self.log.info("Invalid username was verified")
        driver.close()

    def test_valid_username(self):
        """
        - Pre-condition:
            Open start page
        - Steps:
            Fill valid username
            Verify the error message isn't displayed
        """

        # Open start page
        driver = webdriver.Chrome(executable_path="C:\Development\QAComplexApp\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info('Start page was opened')

        # Fill valid username
        username_rg_field = driver.find_element(by=By.XPATH, value='.//input[@id="username-register"]')
        username_rg_field.clear()

        length_username_rg = 2
        username_rg = ''
        for i in range(length_username_rg):
            username_rg += ''.join(self.random_str() + self.random_num())
        username_rg_field.send_keys(username_rg)
        self.log.info('Username was filled')
        sleep(2)

        # Verify the error message isn't displayed
        assert not 'Username must be at least 3 characters.' in driver.page_source
        self.log.info("Invalid username wasn't verified")
        driver.close()

    def test_empty_credentials(self):
        """
        - Pre-condition:
            open start page
        - Steps:
            fill username
            leave empty email
            leave empty password
            click SignUp button
            verify error messages
        """

        # Open start page
        driver = webdriver.Chrome(executable_path="C:\Development\QAComplexApp\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info('Start page was opened')

        # Fill username
        username_rg_field = driver.find_element(by=By.XPATH, value='.//input[@id="username-register"]')
        username_rg_field.clear()

        length_username_rg = 2
        username_rg = ''
        for i in range(length_username_rg):
            username_rg += ''.join(self.random_str() + self.random_num())
        username_rg_field.send_keys(username_rg)
        self.log.info('Username was filled')
        sleep(2)

        # Leave empty email
        email_rg_field = driver.find_element(by=By.XPATH, value='.//input[@id="email-register"]')
        email_rg_field.clear()
        self.log.info('Email was empty')

        # Leave empty password
        password_rg_field = driver.find_element(by=By.XPATH, value='.//input[@id="password-register"]')
        password_rg_field.clear()
        self.log.info('Password was empty')

        # Click SignUp button
        driver.find_element(by=By.XPATH, value=".//button[@type='submit']").click()
        self.log.info("SignUp button was click")

        # Verify error messages
        assert 'You must provide a valid email address.' in driver.page_source
        assert 'Password must be at least 12 characters.' in driver.page_source
        self.log.info("Invalid email, password were verified")
        driver.close()
