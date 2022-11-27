import pytest
import allure
from page.PageYandex import Search


def test_search_yandex(browser):
    main_page = Search(browser)
    main_page.go_to_site()
    main_page.enter_word('Тензор')
    main_page.tab_switch(1)
    main_page.links_tensor()
    main_page.tab_switch(2)
    main_page.check_links()


    



if __name__ == '__main__':
	pytest.main([__file__])

