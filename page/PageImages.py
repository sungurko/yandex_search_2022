from selenium.webdriver.common.keys import Keys
import allure
from page.base_page import Page
from page.locators import Locators



class Images(Page):


    @allure.feature('Проверка ссылки «Картинки» и переход по ней')
    def check_link_image(self):
        with allure.step('Проверить наличие ссылки Картинки'):
            input_search = self.driver.find_element(*Locators.LOCATOR_YANDEX_SEARCH_FIELD)
            input_search.click()
            self.driver.switch_to.frame(self.driver.find_element(*Locators.LOCATOR_YANDEX_SEARCH_FIELD))
            links_images = self.driver.find_element(*Locators.LINK_IMAGE)
            assert links_images, ('Нет ссылки на «Картинки»')
            print('Проверено - ссылка на «Картинки» присутствует')

        with allure.step('Переход по ссылке'):
            links_images.click()
            print('Перешли по ссылке «Картинки»')

    def check_url(self):
        with allure.step('Проверить, что перешли на https://yandex.ru/images'):
            img_url = 'https://yandex.ru/images/'
            assert self.driver.current_url[:len(img_url)] == img_url, ('url отличается')
            print('Проверено - перешли на https://yandex.ru/images')


    def tab_switch(self, value):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[value])
        return tabs

    def current_url(self):
        '''Текущий url'''
        url = self.driver.current_url
        return url


    def click_images(self):
        images_click=self.driver.find_element(*Locators.SEARCH_RESULT)
        images_click.click()
        return images_click


    def open_first_category(self):
        img = self.driver.find_elements(*Locators.IMAGE_FIRST_CATEGORY)
        return img


    def image_search(self):
        input_text = self.driver.find_element(*Locators.CLASS_NAME2)
        return input_text

    def open_first_img(self):
        img = self.driver.find_elements(*Locators.CLASS_NAME1)
        return img