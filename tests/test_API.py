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


def test_get_homes():
    client = app.test_client()
    resp = client.get('/api/v1.0/home', headers={"accept": "application/json", "Authorization": gbl_dict['jwt_token']})
    assert resp.status_code == http.HTTPStatus.OK
    assert len(resp.json) > 0


def test_del_user():
    user = UserService.get_bu_username("test_user")
    resp = UserService.delete_user(user)
    assert resp[1] == 204