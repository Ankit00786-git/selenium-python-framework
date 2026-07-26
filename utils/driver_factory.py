from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.logger import Logger
from config.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver():

        

        logger = Logger.get_logger("DriverFactory")

        

        options = Options()

        if ConfigReader.get_headless():
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")

        logger.info("Launching Chrome browser")

        

        driver = webdriver.Chrome(options=options)

        driver.implicitly_wait(ConfigReader.get_implicit_wait())

        logger.info("Browser launched successfully")

        

        return driver
