from selenium.webdriver.common.keys import Keys
import allure
from page.base_page import Page
from page.locators import Locators



class Search(Page):


    @allure.feature('Проверка поля поиска подсказки suggest')
    def enter_word(self, word):
        with allure.step('Проверить наличия поля поиска'):
            input_search = self.driver.find_element(*Locators.LOCATOR_YANDEX_SEARCH_FIELD)
            assert input_search, f'На странице отсутствует поле поиска'
            print('Проверено - поле поиска имеется')

        with allure.step('Проверить, что появилась таблица с подсказками (suggest)'):
            self.driver.switch_to.frame(self.driver.find_element(*Locators.LOCATOR_YANDEX_SEARCH_FIELD)) # фрейм с категориям
            suggest = self.driver.find_element(*Locators.LOCATOR_YANDEX_MINI_SUGGEST) #панель подсказок
            assert suggest, f'Нет таблицы подсказок'
            print('Проверено - таблица с подсказками (suggest) имеется')

        with allure.step('Вводим в поиске Тензор'):
            suggest.send_keys(word)

        with allure.step('Нажимаем кнопку Enter, появились результаты поиска'):
            button = self.driver.find_element(*Locators.SEARCH_BUTTON)
            button.send_keys(Keys.ENTER)
            print('Нажали кнопку Enter')


    def tab_switch(self, value):
        '''Переключатель вкладок'''
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[value])
        return tabs

    def links_tensor(self):
        '''Переход по ссылке'''
        links=self.driver.find_element(*Locators.SEARCH_RESULT)
        links.click()

    @allure.feature('Проверка поля поиска подсказки suggest')
    def check_links(self):
        with allure.step('Проверить наличия поля поиска'):
            assert self.driver.current_url == 'https://tensor.ru/', ('tensor.ru не найден')
            print('Проерено - 1 ссылка ведет на сайт tensor.ru')



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


    def open_top(self):
        img = self.driver.find_elements(*Locators.CLASS_NAME)
        return img


    def input_text(self):
        input_text = self.driver.find_element(*Locators.CLASS_NAME2)
        return input_text

    def open_img(self):
        img1 = self.driver.find_elements(*Locators.CLASS_NAME1)
        return img1













