from pages.google_page import GooglePage
from config.config_reader import ConfigReader


'''alive is awesome first webhook triggered'''
def test_failure(driver):

    page = GooglePage(driver)

    page.open(ConfigReader.get_base_url())

    assert "Google" in driver.title
