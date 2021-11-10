from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

"""This class is the parent page of pages """
""" contains generic methods and utilities"""


class BasePage:
    MAX_WAIT_TIMEOUT = 30

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.MAX_WAIT_TIMEOUT)

    def get_current_url(self):
        return self.driver.current_url

    def click_on(self, by_locator):
        self.wait.until(expected_conditions.element_to_be_clickable(by_locator)).click()

    def write_on_field(self, field_locator, text):
        field = self.wait.until(expected_conditions.element_to_be_clickable(field_locator))
        field.clear()
        field.send_keys(text)

    def get_text_from(self, by_locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(by_locator)).text

    def get_elements(self, by_locator):
        self.wait.until(expected_conditions.presence_of_element_located(by_locator))
        return self.wait.until(expected_conditions.presence_of_all_elements_located(by_locator))

    def get_element(self, by_locator):
        return self.wait.until(expected_conditions.presence_of_element_located(by_locator))

    def move_to_given_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
