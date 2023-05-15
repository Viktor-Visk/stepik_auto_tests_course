import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class Test_Auth():
    def test_auth_fo_link (self, browser):
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        time.sleep (5)
        button_sing_in = browser.find_element(By.ID, "ember33").click()
        time.sleep (5)
        find_mail = browser.find_element(By.ID, "id_login_email").send_keys("EMail")
        find_pass = browser.find_element(By.ID, "id_login_password").send_keys("Pass")
        button_apply = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
        time.sleep (10)
        
        
