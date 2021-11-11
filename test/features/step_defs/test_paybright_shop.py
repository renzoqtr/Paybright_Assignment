import pytest
from pages.GoogleCAPage import GoogleCAPage
from pages.PayBrightPage import PayBrightPage
from pytest_bdd import scenarios, given, when, then, parsers
from test.features.step_defs.driver_conf import init_driver

scenarios('../paybright_shop.feature')


@pytest.fixture
def web_driver():
    driver = init_driver("CHROME")
    yield driver
    driver.quit()


@given('the google canada page is displayed', target_fixture="google")
def open_google(web_driver):
    google = GoogleCAPage(web_driver)
    google.open_page()
    assert "https://www.google.ca/" in google.get_current_url()
    return google


@given(parsers.parse('user searches for "{phrase}"'))
def google_search(google, phrase):
    google.write_on_google_search_field(phrase)
    google.click_on_google_search_button()


@given(parsers.parse('"{dotcom}" result is displayed'), target_fixture="google_search_result")
def verify_google_result(google, dotcom):
    results_list = google.get_search_results()
    search_result = list(filter(lambda link: dotcom in link.text, results_list))[0]
    assert search_result is not None
    assert search_result.is_displayed()
    return search_result


@when(parsers.parse('user navigates to expected results: "{url}"'), target_fixture="paybright")
def navigate_to_result(web_driver, google_search_result, url):
    google_search_result.click()
    paybright = PayBrightPage(web_driver)
    assert url == paybright.get_current_url()
    return PayBrightPage(web_driver)


@when('user go to shop')
def paybright_go_to_shop(paybright):
    # paybright.click_on_shop_link()
    # wait_until_url_contains(self, contained):
    # paybright.wait_until_loaded()
    pass


@when(parsers.parse('user sorts by "{option}" with merchant "{brand}"'))
def paybright_sort_by(paybright, option, brand):
    paybright.click_on_sort_by()
    paybright.select_option_on_sort_by(option)
    paybright.write_on_search_field(brand)


@then(parsers.parse('"{brand}" card is shown as result'))
def verify_brand(paybright, brand):
    expected_card = paybright.get_result_card(brand)
    paybright.move_to_given_element(expected_card)
    assert expected_card.is_displayed()
