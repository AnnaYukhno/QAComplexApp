import datetime
import logging
import random
import string
from time import sleep


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
