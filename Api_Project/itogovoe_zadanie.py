import requests

class Get_actor_from_star_wars():

    @staticmethod
    def get_and_add_actor_in_file():
        """Получаем информацию по фильмам о Дарт Вейдере"""
        url = 'https://swapi.dev/api/people/4/'
        request_get = requests.get(url)
        request_json = request_get.json()
        print(request_json)

        """Получаем список фильмов, где снимался Дарт Вейдер"""
        vader_movie = request_json['films']
        print("Получили url всех фильмов, где снимался Дарт Вейдер: " + str(vader_movie))

        """Множество для хранения уникальных имен персонажей"""
        character_names = set()

        """Проходим по каждому фильму с дарт Вейдером"""
        for movie_url in vader_movie:
            movie_response = requests.get(movie_url)
            movie_data = movie_response.json()

        """Получаем список персонажей из фильмов"""
        characters = movie_data['characters']
        print("Получили url всех персонажей из фильмов, которые снимались с Дартом Вейдером: " + str(characters))


        """Добавляем имена персонажей во множество"""
        for character_url in characters:
            character_response = requests.get(character_url)
            character_data = character_response.json()
            character_names.add(character_data['name'])

        """Сохраняем имена персонажей в файл"""
        with open('file_character.txt', "w", encoding='utf-8') as file:
            for name in sorted(character_names):
                file.write(name + '\n')
        print("Успех! Персонажи, которые снимались с Дарт Вейдером в одном фильме, были добавлены в текстовый документ")
        print("Список персонажей: " + str(character_names))


    get_and_add_actor_in_file()