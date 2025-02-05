import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Login_page(Base):
    url = "https://upstore24.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    link_authorization = "(//li[@class='user_icons-item js-user_icons-item nav-hide'])[1]"
    user_name = "//input[@id='email']" #test_user_maks@mail.ru
    password = "//input[@id='password']" #test_user_maks
    login_button = "//button[@class='co-button co-form-button js-co-login-submit']"
    main_word = "//h1[@class='co-checkout-title co-title co-title--h1']"

    # Getters

    def get_link_authorization(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.link_authorization)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions
    def click_link_authorization(self):
        self.get_link_authorization().click()
        print("Переход в окно авторизации")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Логин введён")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Пароль введён")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажали кнопку авторизации")

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_link_authorization()
        self.input_user_name("test_user_maks@mail.ru")
        self.input_password("test_user_maks")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "История заказов")