import requests
import allure

from endpoints.constants import BASE_URL


class DeleteObject:
    response = None
    response_json = None

    # Удалить свое животное, статус код 200
    @allure.feature('Удаление объекта')
    @allure.story('Удалить животное, статус код 200')
    def delete_object_200(self, obj_id):
        self.response = requests.delete(f'{BASE_URL}{obj_id}')
        assert self.response.status_code == 200

    # Удалить свое животное еще раз, статус код 404
    @allure.feature('Удаление объекта')
    @allure.story('Удалить животное, статус код 404')
    def delete_object_404(self, obj_id):
        self.response = requests.delete(f'{BASE_URL}{obj_id}')
        assert self.response.status_code == 404

    # Удалить животное с некорректным id, статус код 400
    @allure.feature('Удаление объекта')
    @allure.story('Удалить животное с некорректным id, статус код 400')
    def delete_object_400(self, obj_id):
        self.response = requests.delete(f'{BASE_URL}{obj_id}')
        assert self.response.status_code == 400
