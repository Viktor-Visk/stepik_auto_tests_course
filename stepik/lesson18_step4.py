import pytest
import time
import unittest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class Test_Massage():
    @pytest.mark.parametrize('links', ["lesson/236895/step/1","lesson/236896/step/1","lesson/236897/step/1","lesson/236898/step/1","lesson/236899/step/1","lesson/236903/step/1","lesson/236904/step/1","lesson/236905/step/1"])
    def test_auth_fo_link (self, browser, links):
        link = f"https://stepik.org/{links}"
        browser.get(link)
        time.sleep (5)
        button_sing_in = browser.find_element(By.ID, "ember33").click()
        time.sleep (2)
        find_mail = browser.find_element(By.ID, "id_login_email").send_keys("EMail")
        find_pass = browser.find_element(By.ID, "id_login_password").send_keys("Pass")
        button_apply = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
        time.sleep (10)
        Text_pole = browser.find_element(By.CSS_SELECTOR, '.textarea')
        Text_pole.send_keys(str(math.log(int(time.time()+0.3))))
        time.sleep (2)
        button_apply = browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
        time.sleep (2)
        massage = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        assert massage.text == "Correct!", "massage.text"

if __name__ == "__main__":
    unittest.main()
        
