import http
from globals import gbl_dict
from src.service.user_service import UserService
from src import app


def test_index():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == http.HTTPStatus.FOUND


def test_create_user():
    client = app.test_client()
    json = {"username": "test_user", "password": "secret", "email": "test_user@gmail.com"}
    resp = client.post('/auth/register', json=json)
    assert resp.status_code == http.HTTPStatus.CREATED


def test_login_user():
    client = app.test_client()
    json = {"username": "test_user", "password": "secret", "email": "test_user@gmail.com"}
    resp = client.post('/auth/login', json=json)
    gbl_dict['jwt_token'] = resp.json['jwt_token']
    assert resp.status_code == http.HTTPStatus.OK
    assert len(gbl_dict['jwt_token']) > 0


# ================== Home api tests ====================

def test_get_homes_no_header():
    client = app.test_client()
    resp = client.get('/api/v1.0/home')
    assert resp.json['msg'] == "Missing Authorization Header"
    assert resp.status_code == http.HTTPStatus.UNAUTHORIZED


def test_set_home():
    client = app.test_client()
    json = {"home_name": "test_Home_name"}
    headers = {"accept": "application/json", "Authorization": gbl_dict['jwt_token']}
    resp = client.post('/api/v1.0/home', headers=headers, json=json)
    gbl_dict['home_uuid'] = resp.json['uuid']
    assert resp.status_code == http.HTTPStatus.CREATED
    assert len(gbl_dict['home_uuid']) > 0


def test_update_home():
    client = app.test_client()
    json = {"home_name": "update_test_Home_name"}
    headers = {"accept": "application/json", "Authorization": gbl_dict['jwt_token']}
    resp = client.put(f'/api/v1.0/home/{gbl_dict["home_uuid"]}', headers=headers, json=json)
    assert resp.status_code == http.HTTPStatus.OK
    assert len(resp.json) > 0


def test_get_homes():
    client = app.test_client()
    resp = client.get('/api/v1.0/home', headers={"accept": "application/json", "Authorization": gbl_dict['jwt_token']})
    assert resp.status_code == http.HTTPStatus.OK
    assert len(resp.json) > 0

# ================== Smart meter api tests ====================


def test_set_smart_meter():
    client = app.test_client()
    json = {"meter_name": "test_Meter_name"}
    headers = {"accept": "application/json", "Authorization": gbl_dict['jwt_token']}
    resp = client.post(f'/api/v1.0/home/{gbl_dict["home_uuid"]}/smartmeter', headers=headers, json=json)
    gbl_dict['smart_uuid'] = resp.json['uuid']
    assert resp.status_code == http.HTTPStatus.CREATED
    assert len(resp.json['uuid']) > 0


def test_get_smart_meter():
    client = app.test_client()
    json = {"meter_name": "test_Meter_name"}
    headers = {"accept": "application/json", "Authorization": gbl_dict['jwt_token']}
    resp = client.get(f'/api/v1.0/home/{gbl_dict["home_uuid"]}/smartmeter', headers=headers, json=json)
    assert resp.status_code == http.HTTPStatus.OK
    assert len(resp.json) > 0


def test_update_smart_meter():
    client = app.test_client()
    json = {"meter_name": "update_test_Meter_name"}
    headers = {"accept": "application/json", "Authorization": gbl_dict['jwt_token']}
    resp = client.put(f'/api/v1.0/home/{gbl_dict["home_uuid"]}/smartmeter/{gbl_dict["smart_uuid"]}', headers=headers, json=json)
    assert resp.status_code == http.HTTPStatus.OK
    assert len(resp.json) > 0


def test_delete_smart_meter():
    client = app.test_client()
    resp = client.delete(f'/api/v1.0/home/{gbl_dict["home_uuid"]}/smartmeter/{gbl_dict["smart_uuid"]}')
    assert resp.status_code == http.HTTPStatus.NO_CONTENT


def test_del_user():
    user = UserService.get_bu_username("test_user")
    resp = UserService.delete_user(user)
    assert resp[1] == 204
