from page.base_page import Page
from page.locators import Locators
import time




class Search(Page):

    def check_input_search(self):
        input_search = self.driver.find_elements(*Locators.LOCATOR_YANDEX_SEARCH_FIELD)
        return input_search







    def enter_word(self, word):
        search_field = self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        search_field.click()
        return search_field
