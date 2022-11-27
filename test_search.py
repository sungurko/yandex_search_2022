import pytest
import time

from page.PageYandex import Search

def test_search_yandex(browser):
    main_page = Search(browser)
    main_page.go_to_site() # загрузка главной страницы yandex.ru
    assert main_page.check_input_search(), ('Нет поля поиска')
    assert main_page.enter_word(), ('Нет таблицы подсказок') # ввести в поиск Тензор
    main_page.enter() # нажать кнопку 'Найти'
    main_page.tab_switch(1) # переключиться на вторую вкладку
    main_page.links_tensor() # перейти по первой ссылке
    main_page.tab_switch(2) # переключиться на третью
    assert main_page.current_url() == 'https://tensor.ru/', ('tensor.ru не найден')


class MyPlugin:
	def sessionfinish(self):
		print("*** test report")

if __name__ == '__main__':
	pytest.main([__file__], plugins=[MyPlugin()])

