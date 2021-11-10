from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class GoogleCAPage(BasePage):
    LOGIN_URL = "https://www.google.ca/?hl=en"
    GOOGLE_SEARCH_BUTTON = (By.CSS_SELECTOR, "div[jsname='VlcLAe'] input[aria-label='Google Search']")
    GOOGLE_SEARCH_INPUT = (By.CSS_SELECTOR, "input[title='Search']")
    GOOGLE_SEARCH_RESULTS = (By.CSS_SELECTOR, "div.tF2Cxc div a")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.LOGIN_URL)

    def write_on_google_search_field(self, to_search):
        self.write_on_field(self.GOOGLE_SEARCH_INPUT, to_search)

    def click_on_google_search_button(self):
        self.click_on(self.GOOGLE_SEARCH_BUTTON)

    def get_search_results(self):
        return self.get_elements(self.GOOGLE_SEARCH_RESULTS)
