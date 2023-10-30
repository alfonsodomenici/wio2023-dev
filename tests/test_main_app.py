from http import HTTPStatus
from flask import url_for

def test_welcome(client):
    resp = client.get(url_for('main.welcome'))
    assert resp.status_code == HTTPStatus.OK
    assert resp.text == 'welcome'

def test_login(client):
    resp = client.get(url_for('main.login'))
    assert resp.status_code == HTTPStatus.OK
    assert resp.text == 'login'