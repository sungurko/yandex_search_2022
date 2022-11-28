from selenium.webdriver.common.keys import Keys
import pytest
import time
from page.PageImages import Images


def test_images(browser):

	img_url = 'https://yandex.ru/images/'
	main_page = Images(browser)
	main_page.go_to_site() # загрузка главной страницы yandex.ru
	main_page.check_link_image()
	main_page.tab_switch(1) # переключиться на вторую вкладку
	main_page.check_url() # проверим url
	img = main_page.open_first_category()[0]
	text = img.get_attribute('text')
	img.click()
	time.sleep(5)
	assert text == main_page.image_search().get_attribute('value'), ('Текст в поиске отличается')
	first_img = main_page.open_first_img()[0] # Первая картинка
	first_img.click()
	current_img = main_page.current_url().split('&')[5]
	assert first_img.get_attribute('href').split('&')[3] == current_img, ('Не открылась') 
	second_image=main_page.current_url().split('&')[3]
	first_img.send_keys(Keys.RIGHT)
	time.sleep(3)
	first_img.send_keys(Keys.LEFT)
	time.sleep(5)
	assert main_page.current_url().split('&')[3] == second_image, ('Картинки разные')


if __name__ == '__main__':
	pytest.main([__file__])