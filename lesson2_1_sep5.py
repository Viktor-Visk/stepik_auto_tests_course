from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)
    
    ceckbox1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    ceckbox1.click()

    radio1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

