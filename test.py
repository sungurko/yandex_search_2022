import pytest
import time

from yandex import Search

def test_yandex_search(browser):
    yandex_main_page = Search(browser)

    yandex_main_page.go_to_site()
    time.sleep(15)

    yandex_main_page.enter_word("Тензор")
    time.sleep(15)
    

class MyPlugin:
	def sessionfinish(self):
		print("*** Отчет о завершении теста")

if __name__ == '__main__':
	pytest.main([__file__], plugins=[MyPlugin()])