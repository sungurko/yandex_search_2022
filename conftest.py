import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
	driver = webdriver.Chrome(executable_path="./chromedriver")
	driver.maximize_window()
	driver.delete_all_cookies()
	driver.implicitly_wait(5)
	yield driver
	driver.quit()