from page.base_page import Page
from page.locators import Locators
import time


class Search(Page):

    def check_input_search(self):
        input_search = self.driver.find_elements(*Locators.LOCATOR_YANDEX_SEARCH_FIELD)
        return input_search

    def check_suggest(self):
        '''таблица с подсказками'''
        suggest=self.driver.find_element(*Locators.LOCATOR_YANDEX_SEARCH_FIELD)
        return suggest


#def check_suggest(self):
        '''таблица с подсказками'''
 #       suggest=self.driver.find_element(*MainPageLocators.SUGGEST)
 #       return suggest
    
    def check_suggest(self):
        self.driver.switch_to.frame(self.driver.find_element(*Locators.LOCATOR_YANDEX_SEARCH_FIELD))
        search_field = self.driver.find_element(*Locators.LOCATOR_YANDEX_MINI_SUGGEST)
        return search_field
        #search_field.send_keys()
        time.sleep(5)



    def enter_word(self, word):
        search_field = self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        search_field.click()
        return search_field
