import requests
import allure

from endpoints.constants import BASE_URL


class UpdateObject:
    response = None
    response_json = None

    # Поменять статус объекта на sold, статус код 200
    @allure.feature('Изменение объекта')
    @allure.story('Поменять статус объекта на sold, статус код 200')
    def update_object_200(self, object_id, payload):
        self.response = requests.put(f'{BASE_URL}{object_id}', json=payload)
        assert self.response.status_code == 200

    # Поменять статус объекта на lost, статус код 405
    @allure.feature('Изменение объекта')
    @allure.story('Поменять статус объекта на lost, статус код 405')
    def update_object_405(self, object_id, payload):
        self.response = requests.put(f'{BASE_URL}{object_id}', json=payload)
        assert self.response.status_code == 405

    # Попробовать изменить несуществующий объект, статус код 404
    @allure.feature('Изменение объекта')
    @allure.story('Поменять несуществующий объект, статус код 404')
    def update_object_404(self, object_id, payload):
        self.response = requests.put(f'{BASE_URL}{object_id}', json=payload)
        assert self.response.status_code == 404

    # Попробовать изменить объект с некорректным id, статус код 400
    @allure.feature('Изменение объекта')
    @allure.story('Поменять объект с некорректным id, статус код 400')
    def update_object_400(self, object_id, payload):
        self.response = requests.put(f'{BASE_URL}{object_id}', json=payload)
        assert self.response.status_code == 400







