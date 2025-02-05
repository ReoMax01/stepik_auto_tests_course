import time
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.catalog_page import Catalog_page
from pages.information_order_page import Information_order_page
from pages.login_page import Login_page
from pages.order_page import Order_page


def test_login():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome()

    print("Старт теста по авторизации")
    login = Login_page(driver)
    login.authorization()
    time.sleep(2)

    print("Старт теста по добавлению товара в корзину")
    bp = Catalog_page(driver)
    bp.add_cart_product()
    time.sleep(2)

    print("Старт теста по переходу к оформлению заказа из корзины")
    cp = Cart_page(driver)
    cp.product_in_cart()
    time.sleep(2)

    print("Старт теста по подтверждению заказа")
    op = Order_page(driver)
    op.order_confirm()
    time.sleep(2)

    print("Старт теста по проверке страницы с оформленным заказом")
    iop = Information_order_page(driver)
    iop.information_order()
