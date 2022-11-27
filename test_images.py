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
    assert main_page.current_url()[:25] == 'https://yandex.ru/images/', ('url отличается')
    img = main_page.open_top()[0]
    text = img.get_attribute('text')
    img.click()
    time.sleep(5)
    assert text == main_page.input_text().get_attribute('value'), ('Текст в поиске отличается')
    img1 = main_page.open_img()[0]
    img1.click()
    time.sleep(5)



class MyPlugin:
	def sessionfinish(self):
		print("*** test report")

if __name__ == '__main__':
	pytest.main([__file__], plugins=[MyPlugin()])

