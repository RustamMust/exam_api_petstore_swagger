import requests
import allure

from endpoints.constants import BASE_URL


class CreateObject:
    response = None
    response_json = None

    # Создать полноценный объект, статус 'available', статус код 200
    @allure.feature('Создание объекта')
    @allure.story('Создать полноценный объект, статус код 200')
    def create_object_200(self, payload):
        with allure.step('Создание объекта'):
            self.response = requests.post(BASE_URL, json=payload)
            self.response_json = self.response.json()
            assert self.response.status_code == 200

    # Создать объект, в теле запроса пустой словарь, статус код 405
    @allure.feature('Создание объекта')
    @allure.story('Создать объект, в теле запроса пустой словарь, статус код 405')
    def create_object_405(self, payload):
        with allure.step('Создание объекта c пустым словарем'):
            self.response = requests.post(BASE_URL, json=payload)
            self.response_json = self.response.json()
            assert self.response.status_code == 405

    # Создать объект, без тела запроса, статус код 415
    @allure.feature('Создание объекта')
    @allure.story('Создать объект, без тела запроса, статус код 415')
    def create_object_415(self, payload):
        self.response = requests.post(BASE_URL, json=payload)
        self.response_json = self.response.json()
        assert self.response.status_code == 415

