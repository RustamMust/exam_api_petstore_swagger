import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject
from payloads.payloads import payload_obj_id
from payloads.payloads import payload_create_object_200
from payloads.payloads import payload_update_object_200
from payloads.payloads import payload_update_object_405
from payloads.payloads import payload_update_object_404
from payloads.payloads import payload_update_object_400






#Создать полноценный объект, статус 'available', статус код 200
def test_create_object_200():
    new_object_endpoint = CreateObject()
    new_object_endpoint.create_object_200(payload=payload_create_object_200)


#Создать объект, в теле запроса пустой словарь, статус код 405
def test_create_object_405():
    new_object_endpoint = CreateObject()
    payload = {}
    new_object_endpoint.create_object_405(payload)


#Создать объект, без тела запроса, статус код 415
def test_create_object_415():
    new_object_endpoint = CreateObject()
    new_object_endpoint.create_object_415(payload=None)


#Поменять статус объекта на sold, статус код 200
def test_update_object_200(obj_id):
    update_obj_endpoint = UpdateObject()
    update_obj_endpoint.update_object_200(obj_id, payload_update_object_200)


#Поменять статус объекта на lost, статус код 405
def test_update_object_405(obj_id):
    update_obj_endpoint = UpdateObject()
    update_obj_endpoint.update_object_405(obj_id, payload_update_object_405)


#Попробовать изменить несуществующий объект, статус код 404
def test_update_object_404():
    update_obj_endpoint = UpdateObject()
    obj_id = '1111111111111'
    update_obj_endpoint.update_object_404(obj_id, payload_update_object_404)


#Попробовать изменить объект с некорректным id, статус код 400
def test_update_object_400():
    update_obj_endpoint = UpdateObject()
    obj_id = 'некорректный id'
    update_obj_endpoint.update_object_400(obj_id, payload_update_object_400)


#Найти свое животное в статусе sold, статус код 200
def test_get_object_200():
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_object_200()


#Найти животное в статусе lost, статус код 400
def test_get_object_400():
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_object_400()


#Удалить свое животное, статус код 200
def test_delete_object_200(obj_id):
    delete_obj_endpoint = DeleteObject()
    delete_obj_endpoint.delete_object_200(obj_id)


#Удалить свое животное еще раз, статус код 404
def test_delete_object_404(obj_id):
    delete_obj_endpoint = DeleteObject()
    delete_obj_endpoint.delete_object_404(obj_id)


#Удалить животное с некорректным id, статус код 400
def test_delete_object_400():
    obj_id = '1111111111111111'
    delete_obj_endpoint = DeleteObject()
    delete_obj_endpoint.delete_object_400(obj_id)


