import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_on_page(browser):
    browser.get(link)
    time.sleep (30)
    x = len (browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))
    assert x != 0,'\Кнопка добавления товара в корзину отсутсвует'
