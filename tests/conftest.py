import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject
from payloads.payloads import payload_obj_id


@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    create_object.create_object_200(payload_obj_id)
    return create_object.response_json['id']