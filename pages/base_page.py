from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger
from pathlib import Path
from datetime import datetime

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

    def take_screenshot(self, name="Screenshot"):
        """
        Capture and save a screenshot.
        """

        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"{name}_{timestamp}.png"

        file_path = screenshot_dir / filename

        self.driver.save_screenshot(str(file_path))

        self.logger.info(f"Screenshot saved: {file_path}")

        return str(file_path)
