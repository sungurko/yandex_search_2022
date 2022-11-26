import pytest
import time

from page.PageYandex import Search

def test_search_yandex(browser):
    main_page = Search(browser)
    main_page.go_to_site() # загрузка главной страницы yandex.ru
    assert main_page.check_input_search(), ('Нет поля поиска') # проверка наличия поля поиска

    
    #time.sleep(5)

    main_page.enter_word("Тензор")
    #time.sleep(5)


#def test_search_yandex(self):
#		main_page = page.MainPage(self.driver) # загрузка главной страницы yandex.ru
#		assert main_page.check_input_search(), ('Нет поля поиска')
#		main_page.search_text_element = "Тензор"
#		time.sleep(5)
#		assert main_page.check_suggest(), ('Нет таблицы подсказок')
#		main_page.enter()
#		time.sleep(5)
#		result_page=main_page.top_5_result()
#		assert 'tensor.ru' in result_page, ('tensor.ru не найден')




    

class MyPlugin:
	def sessionfinish(self):
		print("*** Отчет о завершении теста")

if __name__ == '__main__':
	pytest.main([__file__], plugins=[MyPlugin()])

