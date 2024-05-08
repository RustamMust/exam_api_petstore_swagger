import requests
import allure

from endpoints.constants import BASE_URL


class GetObject:
    response = None
    response_json = None

    # Найти свое животное в статусе sold, статус код 200
    @allure.feature('Поиск объекта')
    @allure.story('Найти животное в статусе sold, статус код 200')
    def get_object_200(self):
        self.response = requests.get(f'{BASE_URL}findByStatus?status=sold')
        self.response_json = self.response.json()
        assert self.response.status_code == 200

    # Найти животное в статусе lost, статус код 400
    @allure.feature('Поиск объекта')
    @allure.story('Найти животное в статусе lost, статус код 400')
    def get_object_400(self):
        self.response = requests.get(f'{BASE_URL}findByStatus?status=lost')
        assert self.response.status_code == 400


