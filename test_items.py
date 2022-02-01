import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestOnePage():
    """ Test: class to test coders-at-work page """

    def test_the_page(self, browser):
        """test: test the page"""
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        sklad = browser.find_element(By.CLASS_NAME, "instock.availability")

        assert 'доступно' or 'available' in sklad.text

