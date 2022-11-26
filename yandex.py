from page import Page
from selenium.webdriver.common.by import By
import time


class Locators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, "[class='dzen-search-arrow-common__frame']")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CSS_SELECTOR, "[class='arrow__input mini-suggest__input']")


class Search(Page):

    def enter_word(self, word):
        search_field = self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field