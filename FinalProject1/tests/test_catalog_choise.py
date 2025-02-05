import time
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page
from pages.link_main_page import Main_page


def test_login():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome()

    print("Старт теста по авторизации")
    login = Login_page(driver)
    login.authorization() #Прогон авторизации из login_page
    time.sleep(2)

    print("Старт теста по наличию разделов в каталоге")
    mp = Main_page(driver)
    mp.catalog_choice()
    time.sleep(2)

    # cp = Cart_page(driver)
    # cp.product_confirmation()
    #
    # uip = User_page(driver)
    # uip.user_information_confirm()
    #
    # pay = Payment_page(driver)
    # pay.payment()
    #
    # f = Finish_page(driver)
    # f.finish()
    #
    # print("Finish test 1")
    # time.sleep(1)
    # driver.quit()
