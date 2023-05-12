from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(3)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.ID, "answer")
    y_element.send_keys(y)
      
        
    # Отправляем заполненную форму
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
