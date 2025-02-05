import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Order_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_name_order = "//div[@class='co-basket_item-description']"
    product_price_order = "(//div[@class='co-basket_subtotal-price co-price--current'])[1]"
    price_delivery = "(//div[@class='co-basket_subtotal-price co-price--current'])[2]"
    total_price_order = "//div[@class='co-basket_total-price co-price--current']"
    button_confirm_order = "//button[@class='co-button co-button--checkout js-button-checkout_submit']"
    text_information_order = "(//div[@class='co-title co-title--h2'])[2]"


    # Getters
    def get_product_name_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_name_order)))

    def get_product_price_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price_order)))

    def get_price_delivery(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_delivery)))

    def get_total_price_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.total_price_order)))

    def get_button_confirm_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_confirm_order)))

    def get_text_information_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.text_information_order)))

    #Actions
    def click_button_confirm_order(self):
        self.get_button_confirm_order().click()
        time.sleep(2)
        print("Нажатие кнопки «Подтвердить заказ»")

    # Methods
    def order_confirm(self):
        self.assert_word_product(self.get_product_name_order(), "Смартфон Apple iPhone 15 Pro Max 256 ГБ Натуральный Титан (nano SIM+eSIM)")
        self.assert_word_product(self.get_product_price_order(), "111 990 ₽")
        self.assert_word_product(self.get_price_delivery(), "900 ₽")
        self.assert_word_product(self.get_total_price_order(), "112 890 ₽")
        self.click_button_confirm_order()
        self.driver.execute_script("window.scrollBy(0, 800)")
        self.assert_word_order(self.get_text_information_order(), "Состав заказа")
        print("Тест по подтверждения оформления заказа пройден")

