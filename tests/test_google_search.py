from utils.driver_factory import DriverFactory
from pages.google_page import GooglePage
from config.config_reader import ConfigReader


def test_google_search():

    driver = DriverFactory.get_driver()

    page = GooglePage(driver)

    page.open(ConfigReader.get_base_url())

    page.search("Selenium Python")

    assert "Google" in page.get_title()

    page.quit()
