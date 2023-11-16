from flask import url_for
from http import HTTPStatus
from . import util
import uuid


def test_register_wio(client,db):
    resp = util.register_wio(client,'wio1',"xx-yy-zz",'code1')
    assert resp.status_code == HTTPStatus.CREATED
    json = resp.get_json()
    assert json['wio'] == 'wio1'
    assert json['macaddress'] == "xx-yy-zz"
    assert json['code'] == 'code1'
    assert json['id'] is not None

def test_register_wio_failed(client,db):
    resp = util.register_wio(client)
    assert resp.status_code == HTTPStatus.BAD_REQUEST

def test_all(client,db):
    resp=util.all_wio(client)
    assert resp.status_code == HTTPStatus.OK
    json = resp.get_json()
    assert len(json)==0
    util.register_wio(client,'wio1',uuid.uuid4(),'code1')
    util.register_wio(client,'wio2',uuid.uuid4(),'code2')
    resp=util.all_wio(client)
    assert resp.status_code == HTTPStatus.OK
    json = resp.get_json()
    assert len(json)==2

def test_auth_ok(client,db):
    ma = uuid.uuid1()
    resp = util.register_wio(client,'wio1',ma,'code1')
    token = util.get_access_token(client,ma.__str__())    
    assert token is not None

def test_info(client,db):
    ma = uuid.uuid1()
    resp = util.register_wio(client,'wio1',ma,'code1')
    token = util.get_access_token(client,ma.__str__())
    resp=util.find_wio(client,token)
    assert resp.status_code == HTTPStatus.OK

def test_add_data(client,db):
    ma = uuid.uuid1()
    resp = util.register_wio(client,'wio1',ma,'code1')
    token = util.get_access_token(client,ma.__str__())
    resp=util.add_wio_data(client,token,type='temperatura',value=36.5)
    assert resp.status_code == HTTPStatus.CREATED
    json = resp.get_json()
    assert json['type'] == 'temperatura'
    assert json['value'] == 36.5

def test_view_data(client,db):
    ma = uuid.uuid1()
    resp = util.register_wio(client,'wio1',ma,'code1')
    token = util.get_access_token(client,ma.__str__())
    util.add_wio_data(client,token,type='temperatura',value=36.5)
    util.add_wio_data(client,token,type='temperatura',value=37)
    resp=util.view_wio_data(client,token)
    assert resp.status_code == HTTPStatus.OK
    json = resp.get_json()
    assert len(json) == 2

def test_stats(client,db):
    ma = uuid.uuid1()
    resp = util.register_wio(client,'wio1',ma,'code1')
    token = util.get_access_token(client,ma.__str__())
    util.add_wio_data(client,token,type='temperatura',value=36)
    util.add_wio_data(client,token,type='temperatura',value=37)
    util.add_wio_data(client,token,type='temperatura',value=38)
    resp=util.view_wio_stats(client,token)
    assert resp.status_code == HTTPStatus.OK
    json = resp.get_json()
    assert json is not None
    assert len(json) == 1
    assert json[0]['type'] == 'temperatura'
    assert json[0]['min'] == 36
    assert json[0]['max'] == 38
    assert json[0]['avg'] == 37
