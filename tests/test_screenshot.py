from pages.google_page import GooglePage
from config.config_reader import ConfigReader


def test_take_screenshot(driver):

    page = GooglePage(driver)

    page.open(ConfigReader.get_base_url())

    screenshot = page.take_screenshot("GoogleHome")

    print(f"Screenshot saved at: {screenshot}")

    assert True
