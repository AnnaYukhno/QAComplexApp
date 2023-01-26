import datetime
import logging
import random
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from constants.base import BaseConstants
from pages.text_presets import POST_TEXT


def random_num():
    """Generate random number"""
    return random.choice(string.digits)


def random_str():
    """Generate random string"""
    return random.choice(string.ascii_letters)


def random_text(length, text=''):
    for i in range(length):
        text += ''.join(random_str() + random_num())
    return text


def random_post(length=15, preset=POST_TEXT):
    """Create post text using provided preset"""
    words = preset.split(" ")
    return " ".join((random.choice(words).replace("\n", "") for _ in range(length)))


def wait_until_ok(timeout=5, period=0.25):
    """Retries function until ok (or 5 sec)"""
    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(
                seconds=timeout
            )
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    log.warning(f"Catching:{err}")
                    if datetime.datetime.now() > end_time:
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def create_driver(browser):
    """Creates driver according to provided browser"""
    if browser == BaseConstants.CHROME:
        driver = webdriver.Chrome(executable_path=BaseConstants.CHROME_DRIVER_PATH)
    elif browser == BaseConstants.FIREFOX:
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=BaseConstants.FF_DRIVER_PATH, options=options)
    else:
        raise ValueError(f"Unknown browser name: {browser}")
    driver.get(BaseConstants.URL)
    driver.implicitly_wait(1)
    return driver
