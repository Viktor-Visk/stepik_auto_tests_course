from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

try:
    link = "https://dev.dev-eq.ru/"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.set_window_size(1920, 1080)
    browser.get(link)
    

    button1 = browser.find_element(By.CSS_SELECTOR, ".app-auth-form-card--filled > .app-auth-form-card__subtitle")
    button1.click()
    # ждем загрузки страницы

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, 'input_15')
    input1.send_keys("qweewq")
    input2 = browser.find_element(By.ID, 'input_16')
    input2.send_keys("qwerty123")
    button2 = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
