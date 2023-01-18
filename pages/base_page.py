from selenium.webdriver.common.by import By


class BasePage:
    """Describes base methods for the website"""

    def __init__(self, driver):
        self.driver = driver

    def fill_fields(self, xpath, value):
        """Fill the fields using provided values"""
        field = self.driver.find_element(by=By.XPATH, value=xpath)
        field.clear()
        field.send_keys(value)

    def click(self, xpath):
        """Find and click on the element by provided xpath"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.click()

    def compare_element_text(self, xpath, text):
        """Compare element text to provided one"""
        element_text = self.driver.find_element(by=By.XPATH, value=xpath)
        return element_text.text == text