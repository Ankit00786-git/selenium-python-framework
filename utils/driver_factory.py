from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver():

        options = Options()

        if ConfigReader.get_headless():
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)

        driver.implicitly_wait(ConfigReader.get_implicit_wait())

        return driver
