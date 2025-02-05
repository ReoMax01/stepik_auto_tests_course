import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver


    """Метод получения url страницы"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Текущий URL: " + get_url)


    """Метод сравнения текста на странице после авторизации"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Пользователь авторизован. Текст «История заказов» совпадает!")


    """Метод сравнения текста продукта (название/цена)на любой странице"""

    def assert_word_product(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Текст верный")

    """Метод сравнения текста на странице с заказом"""
    def assert_word_order(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Заказ оформлен. Открыта страница с информацией об оформленном заказе")

    """Метод создания скриншота"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('F:\\LearningPython\\finalProject\\screen\\' + name_screenshot)

    """Метод сравнения URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL верное: ", self.driver.current_url)

