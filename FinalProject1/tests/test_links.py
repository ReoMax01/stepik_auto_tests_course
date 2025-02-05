import time
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page
from tests.test_catalog_choise import Main_page


def test_login():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome()

    print("Старт теста по авторизации")
    login = Login_page(driver)
    login.authorization()
    time.sleep(2)

    print("Старт теста по наличию разделов в главном меню")
    mp = Main_page(driver)
    mp.link_main_page()
    time.sleep(2)