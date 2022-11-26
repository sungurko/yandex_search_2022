from BasePage import Page
from selenium.webdriver.common.by import By
import time


class Locators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, "[class='dzen-search-arrow-common__frame']")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CSS_SELECTOR, "[class='arrow__input mini-suggest__input']")


class Search(Page):

    def check_input_search(self):
        input_search = self.driver.find_elements(*Locators.LOCATOR_YANDEX_SEARCH_FIELD)
        #input_search.click()
        return input_search







    def enter_word(self, word):
        search_field = self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        #search_field.click()
        return search_field