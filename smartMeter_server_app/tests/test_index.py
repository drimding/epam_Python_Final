import http

from smartMeter_server_app import app


def test_index():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == http.HTTPStatus.OK
