import pytest
import time

from page.PageYandex import Search

def test_images(browser):
    main_page = Search(browser)
    main_page.go_to_site() # загрузка главной страницы yandex.ru
    main_page.input_search()
    time.sleep(5)
    assert main_page.check_link_images(), ('Нет ссылки на картинки') # проверка наличи ссылки «Картинки»
    time.sleep(5)
    main_page.tab_switch(1) # переключиться на вторую вкладку


    

class MyPlugin:
	def sessionfinish(self):
		print("*** test report")

if __name__ == '__main__':
	pytest.main([__file__], plugins=[MyPlugin()])

