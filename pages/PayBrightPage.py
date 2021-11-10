from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.BasePage import BasePage


class PayBrightPage(BasePage):
    PAYBRIGHT_SHOP_LINK = (By.XPATH, ".//nav[@type='primary']//a[contains(.,'Shop')]")
    PAYBRIGHT_SORT_BY_DP = (By.ID, "mui-component-select-sort-by")
    PAYBRIGHT_SORT_BY_OPTIONS = (By.CSS_SELECTOR, "div.MuiPopover-paper >ul>li")
    PAYBRIGHT_SEARCH_FIELD = (By.NAME, "search")
    PAYBRIGHT_RESULT_CARDS = (By.CSS_SELECTOR, "div.styles__MerchantCardWrapper-sc-1m5ue4o-14")
    PAYBRIGHT_RESULT_CARD = ".//a[contains(., 'brand')]"

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_shop_link(self):
        self.click_on(self.PAYBRIGHT_SHOP_LINK)

    def click_on_sort_by(self):
        self.click_on(self.PAYBRIGHT_SORT_BY_DP)

    def write_on_search_field(self, search):
        self.write_on_field(self.PAYBRIGHT_SEARCH_FIELD, search)

    def select_option_on_sort_by(self, desired_option):
        options = self.get_elements(self.PAYBRIGHT_SORT_BY_OPTIONS)
        located_option = list(filter(lambda option: desired_option in option.text, options))[0]
        located_option.click()

    def wait_for_any_result(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.PAYBRIGHT_RESULT_CARDS))

    def get_result_card(self, brand):
        locator = self.PAYBRIGHT_RESULT_CARD.replace("brand", brand)
        return self.get_element((By.XPATH, locator))

    def get_result_cards(self):
        return self.get_elements(self.PAYBRIGHT_RESULT_CARDS)
