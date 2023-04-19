from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button1 = browser.find_element(By.ID, "button")
    button1.click()

        
    # Отправляем заполненную форму
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
