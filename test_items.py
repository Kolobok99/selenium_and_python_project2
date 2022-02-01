import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestOnePage():
    """ Test: class to test coders-at-work page """

    def test_the_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        message = browser.find_element(By.ID, "messages")
        time.sleep(15)
        print(message)