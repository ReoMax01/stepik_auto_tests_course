import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_name_cart = "//div[@class='cart-item-title']"
    product_price_cart = "//div[@class='cart-item-total_price js-cart-item-total_price']"
    product_price_cart_total = "//span[@class='cart-order-total_price js-cart-order-total_price']"
    button_place_order = "//input[@class='button button--primary button--block button--large']"


    # Getters
    def get_product_name_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_name_cart)))

    def get_product_price_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price_cart)))

    def get_product_price_cart_total(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price_cart_total)))

    def get_button_place_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_place_order)))

    #Actions
    def click_button_place_order(self):
        self.get_button_place_order().click()
        time.sleep(2)
        print("Переход в окно подтверждения заказа")

    # Methods
    def product_in_cart(self):
        self.assert_word_product(self.get_product_name_cart(), "Смартфон Apple iPhone 15 Pro Max 256 ГБ Натуральный Титан (nano SIM+eSIM)")
        self.assert_word_product(self.get_product_price_cart(), "111 990 ₽")
        self.assert_word_product(self.get_product_price_cart_total(), "111 990 ₽")
        self.click_button_place_order()
        self.assert_url("https://upstore24.ru/new_order")
        print("Тест по переходу из корзины в окно оформления заказа пройден")
