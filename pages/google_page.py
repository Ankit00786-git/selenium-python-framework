from pages.base_page import BasePage
from locators.google_locators import GoogleLocators


class GooglePage(BasePage):

    def search(self, text):
        self.enter_text(
            GoogleLocators.SEARCH_BOX,
            text
        )
