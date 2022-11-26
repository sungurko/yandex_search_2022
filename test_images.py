import pytest
import time

from page.PageYandex import Search

def test_images(browser):
    main_page = Search(browser)
    main_page.go_to_site() # загрузка главной страницы yandex.ru
    


    

class MyPlugin:
	def sessionfinish(self):
		print("*** test report")

if __name__ == '__main__':
	pytest.main([__file__], plugins=[MyPlugin()])

