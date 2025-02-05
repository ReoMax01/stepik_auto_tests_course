import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_catalog = "(//a[text()='Каталог'])[3]"
    catalog_smartphones = "(//a[@data-target='18202166'])[3]"
    button_sort = "//select[@class='js-filter-sort input--sort']"
    product_name_1 = "(//div[@class='product_card-title'])[1]"
    product_name_1_modalka = "//div[@class='message-cart-product-title']"
    product_price_1_modalka = "//div[@class='message-cart-product-quantity']"
    button_add_cart_1 = "(//button[@class='button button--icon button--small button--empty button--empty--inverse'])[1]"
    button_close_modalka = "(//button[@title='Close'])[2]"
    button_cart = "(//li[@class='user_icons-item js-user_icons-item'])[3]"
    sort_by_popularity = "//option[text()='По популярности']"
    sort_by_high_price = "//option[text()='По возрастанию цены']"
    sort_by_low_price = "//option[text()='По убыванию цены']"
    sort_by_new = "//option[text()='По новинкам']"
    sort_by_discount = "//option[text()='По скидке']"
    sort_by_title = "//option[text()='По алфавиту']"
    sort_by_default = "//option[text()='По умолчанию']"

    # Getters
    def get_button_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_catalog)))

    def get_catalog_smartphones(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_smartphones)))

    def get_button_sort(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_sort)))

    def get_sort_by_popularity(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_popularity)))

    def get_sort_by_high_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_high_price)))

    def get_sort_by_low_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_low_price)))

    def get_sort_by_new(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_new)))

    def get_sort_by_discount(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_discount)))

    def get_sort_by_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_title)))

    def get_sort_by_default(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_default)))

    def get_product_name_1_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_name_1)))

    def get_product_name_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_name_1)))

    def get_product_name_1_modalka(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_name_1_modalka)))

    def get_button_add_cart_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_add_cart_1)))

    def get_button_close_modalka(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_close_modalka)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_product_price_1_modalka(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price_1_modalka)))


    #Actions
    def click_button_catalog(self):
        self.get_button_catalog().click()
        time.sleep(2)
        print("Переход в окно «Каталог»")

    def click_catalog_smartphones(self):
        self.get_catalog_smartphones().click()
        self.driver.execute_script("window.scrollBy(0, 600)")
        print("Открытие каталога «Смартфоны». Скролл страницы до выпадающего списка сортировки товаров")

    def click_button_sort(self):
        self.get_button_sort().click()
        time.sleep(2)
        print("Нажатие на выпадающие список «Сортировать»")

    def click_sort_by_popularity(self):
        self.get_sort_by_popularity().click()
        time.sleep(2)
        print("Нажатие на сортировку «По популярности»")

    def click_sort_by_high_price(self):
        self.get_sort_by_high_price().click()
        time.sleep(2)
        print("Нажатие на сортировку «По возрастанию цены»")

    def click_sort_by_low_price(self):
        self.get_sort_by_low_price().click()
        time.sleep(2)
        print("Нажатие на сортировку «По убыванию цены»")

    def click_sort_by_new(self):
        self.get_sort_by_new().click()
        time.sleep(2)
        print("Нажатие на сортировку «По новинкам»")

    def click_sort_by_discount(self):
        self.get_sort_by_discount().click()
        time.sleep(2)
        print("Нажатие на сортировку «По скидке»")

    def click_sort_by_title(self):
        self.get_sort_by_title().click()
        time.sleep(2)
        print("Нажатие на сортировку «По алфавиту»")

    def click_sort_by_default(self):
        self.get_sort_by_default().click()
        time.sleep(2)
        print("Нажатие на сортировку «По умолчанию»")

    def click_button_add_cart_1(self):
        self.get_button_add_cart_1().click()
        time.sleep(2)
        print("Добавление товара в корзину")

    def click_button_close_modalka(self):
        self.get_button_close_modalka().click()
        time.sleep(2)
        print("Добавление товара в корзину")

    def click_button_cart(self):
        self.get_button_cart().click()
        time.sleep(2)
        print("Добавление товара в корзину")

    # Methods
    def sortirovka(self):
        self.click_button_catalog()
        self.click_catalog_smartphones()
        self.click_button_sort()
        self.click_sort_by_popularity()
        self.assert_url("https://upstore24.ru/collection/phones?order=descending_popularity")
        self.click_button_sort()
        self.click_sort_by_high_price()
        self.assert_url("https://upstore24.ru/collection/phones?order=price")
        self.click_button_sort()
        self.click_sort_by_low_price()
        self.assert_url("https://upstore24.ru/collection/phones?order=descending_price")
        self.click_button_sort()
        self.click_sort_by_new()
        self.assert_url("https://upstore24.ru/collection/phones?order=descending_age")
        self.click_button_sort()
        self.click_sort_by_discount()
        self.assert_url("https://upstore24.ru/collection/phones?order=descending_discount")
        self.click_button_sort()
        self.click_sort_by_title()
        self.assert_url("https://upstore24.ru/collection/phones?order=title")
        self.click_button_sort()
        self.click_sort_by_default()
        self.assert_url("https://upstore24.ru/collection/phones")
        print("Тест по сортировке пройден")

    def add_cart_product(self):
        self.click_button_catalog()
        self.click_catalog_smartphones()
        self.click_button_add_cart_1()
        self.assert_word_product(self.get_product_name_1_modalka(), "Смартфон Apple iPhone 15 Pro Max 256 ГБ Натуральный Титан (nano SIM+eSIM)")
        self.assert_word_product(self.get_product_price_1_modalka(), "1 × 111 990 ₽")
        self.click_button_close_modalka()
        self.click_button_cart()
        self.assert_url("https://upstore24.ru/cart_items")
        print("Тест по добавлению товара в корзину пройден")

