from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    id_1_element = browser.find_element(By.ID, "num1")
    text_id_1 = id_1_element.text
    id_1 = int(text_id_1)
    print (id_1)
    id_2_element = browser.find_element(By.ID, "num2")
    text_id_2 = id_2_element.text
    id_2 = int(text_id_2)
    print (id_2)
    z = id_1 + id_2
    z_str= str(z)
    print (z)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))
    

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

