from page.base_page import Page
from page.locators import Locators
import time


class Search(Page):

    def check_input_search(self):
        '''Поле ввода'''
        input_search = self.driver.find_element(*Locators.LOCATOR_YANDEX_SEARCH_FIELD)
        return input_search

    def enter_word(self, word = 'Тензор'):
        '''Сделал аргумент по-умолчанию, т.к. использовал для проверки наличия панели подсказок'''
        self.driver.switch_to.frame(self.driver.find_element(*Locators.LOCATOR_YANDEX_SEARCH_FIELD)) # фрейм с категориями
        search = self.driver.find_element(*Locators.LOCATOR_YANDEX_MINI_SUGGEST) # панель подсказок
        search.send_keys(word)
        return search

    def enter(self):
        '''Нажатие кнопки Найти'''
        button = self.driver.find_element(*Locators.SEARCH_BUTTON)
        button.click()
        return button

    def tab_switch(self, value):
        '''Переключатель вкладок'''
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[value])
        return tabs

    def links_tensor(self):
        '''Переход по ссылке'''
        links=self.driver.find_element(*Locators.SEARCH_RESULT)
        links.click()
        return links

    def current_url(self):
        '''Текущий url'''
        url = self.driver.current_url
        return url

    '''images'''

    def input_search(self):
        search_field = self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        return search_field

    def check_link_images(self):
        self.driver.switch_to.frame(self.driver.find_element(*Locators.LOCATOR_YANDEX_SEARCH_FIELD))
        links_images = self.driver.find_element(*Locators.LINK_IMAGE)
        links_images.click()
        return links_images

    def click_images(self):
        images_click=self.driver.find_element(*Locators.SEARCH_RESULT)
        images_click.click()
        return images_click













