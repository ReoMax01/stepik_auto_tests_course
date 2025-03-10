"""Методы для проверки ответов на запросы"""
import json

class Checking():

    """Метод для проверки статус кода запроса"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        if result.status_code == status_code:
            print("Успешно!!! Статус код = " + str(result.status_code))
        else:
            print("Ошибка!!! Статус код = " + str(result.status_code))


    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("Успех! Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен!!!")