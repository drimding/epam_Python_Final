import http

from src import app


def test_index():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == http.HTTPStatus.FOUND
