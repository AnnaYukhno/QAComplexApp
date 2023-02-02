import pytest

from pages.start_page import StartPage
from pages.utils import create_driver
from pages.values import User


@pytest.fixture()
def driver(browser):
    """Create selenium driver"""
    driver = create_driver(browser=browser)
    yield driver
    driver.close()


@pytest.fixture()
def start_page(driver):
    """Create start page object"""
    return StartPage(driver)


@pytest.fixture()
def empty_user():
    """Create empty user"""
    return User()


@pytest.fixture()
def random_user(empty_user):
    """Create random user"""
    empty_user.fill_data()
    return empty_user
