import requests
import pytest

@pytest.fixture()
def obj_id():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.post('https://petstore.swagger.io/v2/pet', json=payload).json()
    yield response['id']
    requests.delete(f'https://petstore.swagger.io/v2/pet/{response['id']}')


#Создать полноценный объект, статус 'available', статус код 200
def test_create_object():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = requests.post('https://petstore.swagger.io/v2/pet', json=payload)
    assert response.status_code == 200
    print(response)


#Создать объект, в теле запроса пустой словарь, статус код 405
def test_create_object_405():
    payload = {}
    response = requests.post('https://petstore.swagger.io/v2/pet', json=payload)
    assert response.status_code == 405


#Создать объект, без тела запроса, статус код 415
def test_create_object_415():
    response = requests.post('https://petstore.swagger.io/v2/pet')
    assert response.status_code == 415


#Поменять статус объекта на sold, статус код 200
def test_update_object_200(obj_id):
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "sold"
    }
    response = requests.put(f'https://petstore.swagger.io/v2/pet/{obj_id}', json=payload)
    assert response.status_code == 200


#Поменять статус объекта на lost, статус код 405
def test_update_object_405(obj_id):
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "lost"
    }
    response = requests.put(f'https://petstore.swagger.io/v2/pet/{obj_id}', json=payload)
    assert response.status_code == 405


#Попробовать изменить несуществующий объект, статус код 404
def test_update_object_404():
    obj_id = '1111111111111'
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "lost"
    }
    response = requests.put(f'https://petstore.swagger.io/v2/pet/{obj_id}', json=payload)
    assert response.status_code == 404


#Попробовать изменить объект с некорректным id, статус код 400
def test_update_object_400():
    obj_id = 'некорректный id'
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "lost"
    }
    response = requests.put(f'https://petstore.swagger.io/v2/pet/{obj_id}', json=payload)
    assert response.status_code == 400


#Найти свое животное в статусе sold, статус код 200
def test_get_object_sold():
    response = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status=sold')
    assert response.status_code == 200


#Найти животное в статусе lost, статус код 400
def test_get_object_lost():
    response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=lost')
    assert response.status_code == 400


#Удалить свое животное, статус код 200
def test_delete_object(obj_id):
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{obj_id}')
    assert response.status_code == 200


#Удалить свое животное еще раз, статус код 404
def test_delete_object_404(obj_id):
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{obj_id}')
    assert response.status_code == 404


#Удалить животное с некорректным id, статус код 400
def test_delete_object_400():
    obj_id = 'некорректный id'
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{obj_id}')
    assert response.status_code == 400


