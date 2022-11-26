from selenium.webdriver.common.by import By


class Locators:
	LOCATOR_YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, "[class='dzen-search-arrow-common__frame']") # поле поиска
	LOCATOR_YANDEX_MINI_SUGGEST = (By.CSS_SELECTOR, "[class='arrow__input mini-suggest__input']") # панель подсказок
	SEARCH_BUTTON = (By.CSS_SELECTOR, "[class='arrow__button']") # кнопка найти
	SEARCH_RESULT = (By.XPATH, "//*[@id='search-result']/li[1]/div/div[1]/div[1]/a/h2/span") # результаты поиска