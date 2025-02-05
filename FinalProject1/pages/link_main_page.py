import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_catalog = "(//a[text()='Каталог'])[2]"
    button_about = "(//a[text()='О нас'])[2]"
    button_warranty = "(//a[text()='Гарантия'])[2]"
    button_contacts = "(//a[text()='Контакты'])[2]"
    button_delivery = "(//a[text()='Доставка'])[2]"
    button_payment = "(//a[text()='Оплата'])[2]"
    button_client_account = "(//a[text()='Личный кабинет'])[2]"
    catalog_smartphones = "(//a[@data-target='18202166'])[3]"
    catalog_planshet = "(//a[@data-target='18202307'])[3]"
    catalog_notebook = "(//a[@data-target='18202336'])[3]"
    catalog_computer = "(//a[@data-target='18771934'])[3]"
    catalog_smart_watch = "(//a[@data-target='18202354'])[3]"
    catalog_play_station = "(//a[@data-target='17234830'])[3]"
    catalog_vr_helmet = "(//li[@data-collection-id='29189322'])[2]"
    catalog_audio = "(//a[@data-target='18202360'])[3]"
    catalog_quadro_copter = "(//a[@data-target='18858698'])[3]"
    catalog_photo_and_video = "(//a[@data-target='20631098'])[3]"
    catalog_video_card = "(//li[@data-collection-id='18202381'])[2]"
    catalog_gadgets = "(//a[@data-target='19306593'])[3]"
    catalog_accessory = "(//a[@data-target='18202384'])[3]"
    catalog_dyson = "(//a[@data-target='30321748'])[3]"
    catalog_maining = "(//li[@data-collection-id='29229619'])[2]"
    catalog_services = "(//li[@data-collection-id='27351754'])[2]"
    main_word = "//h1[@class='section-title']"

    # Getters

    def get_button_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_catalog)))

    def get_button_about(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_about)))

    def get_button_warranty(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_warranty)))

    def get_button_contacts(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_contacts)))

    def get_button_delivery(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_delivery)))

    def get_button_payment(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_payment)))

    def get_button_client_account(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_client_account)))

    def get_catalog_smartphones(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_smartphones)))

    def get_catalog_planshet(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_planshet)))

    def get_catalog_notebook(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_notebook)))

    def get_catalog_computer(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_computer)))

    def get_catalog_smart_watch(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_smart_watch)))

    def get_catalog_play_station(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_play_station)))

    def get_catalog_vr_helmet(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_vr_helmet)))

    def get_catalog_audio(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_audio)))

    def get_catalog_quadro_copter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_quadro_copter)))

    def get_catalog_photo_and_video(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_photo_and_video)))

    def get_catalog_video_card(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_video_card)))

    def get_catalog_gadgets(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_gadgets)))

    def get_catalog_accessory(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_accessory)))

    def get_catalog_dyson(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_dyson)))

    def get_catalog_maining(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_maining)))

    def get_catalog_services(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_services)))

    def get_catalog_word(self,):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #Actions
    def click_button_about(self):
        self.get_button_about().click()
        time.sleep(2)
        print("Переход в окно «О нас»")

    def click_button_warranty(self):
        self.get_button_warranty().click()
        time.sleep(2)
        print("Переход в окно «Гарантия»")

    def click_button_contacts(self):
        self.get_button_contacts().click()
        time.sleep(2)
        print("Переход в окно «Контакты»")

    def click_button_delivery(self):
        self.get_button_delivery().click()
        time.sleep(2)
        print("Переход в окно «Доставка»")

    def click_button_payment(self):
        self.get_button_payment().click()
        time.sleep(2)
        print("Переход в окно «Оплата»")

    def click_button_client_account(self):
        self.get_button_client_account().click()
        time.sleep(2)
        print("Переход в окно «Личный кабинет»")

    def click_button_catalog(self):
        self.get_button_catalog().click()
        print("Переход в окно «Каталог» с каталогом товаров")

    def click_catalog_smartphones(self):
        self.get_catalog_smartphones().click()
        print("Открытие каталога «Смартфоны»")

    def click_catalog_planshet(self):
        self.get_catalog_planshet().click()
        print("Открытие каталога «Планшеты»")

    def click_catalog_notebook(self):
        self.get_catalog_notebook().click()
        print("Открытие каталога «Ноутбуки»")

    def click_catalog_computer(self):
        self.get_catalog_computer().click()
        print("Открытие каталога «Компьютеры»")

    def click_catalog_smart_watch(self):
        self.get_catalog_smart_watch().click()
        print("Открытие каталога «Смарт часы и браслеты»")

    def click_catalog_play_station(self):
        self.get_catalog_play_station().click()
        print("Открытие каталога «Игровые приставки»")

    def click_catalog_vr_helmet(self):
        self.get_catalog_vr_helmet().click()
        print("Открытие каталога «Шлемы виртуальной реальности»")

    def click_catalog_audio(self):
        self.get_catalog_audio().click()
        print("Открытие каталога «Аудио»")

    def click_catalog_quadro_copter(self):
        self.get_catalog_quadro_copter().click()
        print("Открытие каталога «Квадрокоптеры и аксессуары»")

    def click_catalog_photo_and_video(self):
        self.get_catalog_photo_and_video().click()
        print("Открытие каталога «Фото и видео»")

    def click_catalog_video_card(self):
        self.get_catalog_video_card().click()
        print("Открытие каталога «Видеокарты»")

    def click_catalog_gadgets(self):
        self.get_catalog_gadgets().click()
        print("Открытие каталога «Гаджеты»")

    def click_catalog_accessory(self):
        self.get_catalog_accessory().click()
        print("Открытие каталога «Аксессуары»")

    def click_catalog_dyson(self):
        self.get_catalog_dyson().click()
        print("Открытие каталога «DYSON»")

    def click_catalog_maining(self):
        self.get_catalog_maining().click()
        print("Открытие каталога «Майнинг»")

    def click_catalog_services(self):
        self.get_catalog_services().click()
        print("Открытие каталога «Услуги»")


    # Methods
    def catalog_choice(self):
        self.click_button_catalog()
        self.assert_url("https://upstore24.ru/collection/all")
        self.click_catalog_smartphones()
        self.assert_url("https://upstore24.ru/collection/phones")
        self.click_catalog_planshet()
        self.assert_url("https://upstore24.ru/collection/tablets")
        self.click_catalog_notebook()
        self.assert_url("https://upstore24.ru/collection/computers")
        self.click_catalog_computer()
        self.assert_url("https://upstore24.ru/collection/pc")
        self.click_catalog_smart_watch()
        self.assert_url("https://upstore24.ru/collection/watches")
        self.click_catalog_play_station()
        self.assert_url("https://upstore24.ru/collection/console")
        # self.click_catalog_vr_helmet()
        # self.assert_url("https://upstore24.ru/collection/vr")
        self.click_catalog_audio()
        self.assert_url("https://upstore24.ru/collection/audio")
        self.click_catalog_quadro_copter()
        self.assert_url("https://upstore24.ru/collection/quadcopters")
        self.click_catalog_photo_and_video()
        self.assert_url("https://upstore24.ru/collection/foto_video")
        self.click_catalog_video_card()
        self.assert_url("https://upstore24.ru/collection/gpu")
        self.click_catalog_gadgets()
        self.assert_url("https://upstore24.ru/collection/gadgets")
        self.click_catalog_accessory()
        self.assert_url("https://upstore24.ru/collection/accessories")
        self.click_catalog_dyson()
        self.assert_url("https://upstore24.ru/collection/dyson")
        self.click_catalog_maining()
        self.assert_url("https://upstore24.ru/collection/crypto")
        self.click_catalog_services()
        self.assert_url("https://upstore24.ru/collection/service")

    def link_main_page(self):
        self.click_button_about()
        self.assert_url("https://upstore24.ru/page/about-us")
        self.click_button_warranty()
        self.assert_url("https://upstore24.ru/page/warranty")
        self.click_button_contacts()
        self.assert_url("https://upstore24.ru/page/contacts")
        self.click_button_delivery()
        self.assert_url("https://upstore24.ru/page/delivery")
        self.click_button_payment()
        self.assert_url("https://upstore24.ru/page/payment")
        self.click_button_client_account()
        self.assert_url("https://upstore24.ru/client_account/orders")
