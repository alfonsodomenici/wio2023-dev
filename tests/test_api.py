from flask import url_for
from http import HTTPStatus

def test_all(client):
    resp=client.get(url_for('api.all'))
    assert resp.status_code == HTTPStatus.OK
    json = resp.get_json()
    assert len(json)==2