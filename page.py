from selenium import webdriver
import pytest




driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://yandex.ru/')