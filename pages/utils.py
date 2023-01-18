import random
import string


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
