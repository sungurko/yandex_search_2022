import pytest
import time

from page.PageYandex import Search

def test_search_yandex(browser):
    main_page = Search(browser)
    main_page.go_to_site() # загрузка главной страницы yandex.ru
    assert main_page.check_input_search(), ('Нет поля поиска') # проверка наличия поля поиска
    time.sleep(15)
    main_page.enter_word("Тензор") # ввести в поиск Тензор
    time.sleep(5)
    assert main_page.check_suggest(), ('Нет таблицы подсказок')
    main_page.enter()
    time.sleep(15)


    

class MyPlugin:
	def sessionfinish(self):
		print("*** test report")

if __name__ == '__main__':
	pytest.main([__file__], plugins=[MyPlugin()])

