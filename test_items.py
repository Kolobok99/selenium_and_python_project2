import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestOnePage():
    """ Test: class to test coders-at-work page """

    def test_add_button(self, browser):
        """test: test the page"""
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        add_button = browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
        
        
        assert len(add_button) != 0, "Кнопка не найдена"        
        assert len(add_button) == 1, "Селектор не уникален!"
