import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Information_order_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_name_order = "//td[@data-title='Наименование']"
    product_price_order = "//td[@data-title='Стоимость']"
    price_delivery = "//td[@data-title='Доставка']"
    total_price_order = "//div[@class='co-order_history-total_sum co-price']"


    # Getters
    def get_product_name_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_name_order)))

    def get_product_price_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price_order)))

    def get_price_delivery(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_delivery)))

    def get_total_price_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.total_price_order)))


    # Methods
    def information_order(self):
        self.assert_word_product(self.get_product_name_order(), "Смартфон Apple iPhone 15 Pro Max 256 ГБ Натуральный Титан (nano SIM+eSIM)")
        self.assert_word_product(self.get_product_price_order(), "111 990 ₽")
        self.assert_word_product(self.get_price_delivery(), "900 ₽")
        self.assert_word_product(self.get_total_price_order(), "112 890 ₽")
        print("Тест по оформлению заказа пройден")

