from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, "[class='dzen-search-arrow-common__frame']") # поле поиска
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CSS_SELECTOR, "[class='arrow__input mini-suggest__input']") # кнопка найти
