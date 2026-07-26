from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = Logger.get_logger(self.__class__.__name__)
    def open(self, url):
        self.logger.info(f"Opening URL: {url}")        
        self.driver.get(url)

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        self.logger.info(f"Entering text into: {locator}")
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def is_displayed(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def get_title(self):
        return self.driver.title

    def quit(self):
        self.logger.info("Closing browser")
        self.driver.quit()
