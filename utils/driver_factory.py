from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    """
    Creates and returns WebDriver instances.
    """

    @staticmethod
    def get_driver(headless=True):
        options = Options()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)

        driver.maximize_window()
        driver.implicitly_wait(10)

        return driver
