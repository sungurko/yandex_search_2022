from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, "[class='dzen-search-arrow-common__frame']") # поле поиска
    LOCATOR_YANDEX_MINI_SUGGEST = (By.CSS_SELECTOR, "[class='arrow__input mini-suggest__input']") # кнопка найти


    #SUGGEST_TABLE = (By.CSS_SELECTOR, "[class='mini-suggest__popup-content']")
	#IFRAME_LINK = (By.CSS_SELECTOR, "[class='dzen-search-arrow-common__frame']")
	# SEARCH_FIELD_IN_IFRAME = (By.CSS_SELECTOR, "[class='arrow__input mini-suggest__input']")