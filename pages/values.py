"""Stores value objects related to the product"""

from pages.utils import random_text


class User:

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password

    def fill_data(self):
        """Fill data by random generated text"""
        self.username = f"{random_text(length=5)}"
        self.email = f"{self.username}@mail.com"
        self.password = f"{self.username}PwD"

    def __repr__(self):
        return f'User:(username={self.username}, email={self.email}@gmail.com, password={self.password})'
