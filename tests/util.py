from flask import url_for

def register_wio(test_client,wio,macaddress,code):
    return test_client.post(
        url_for('api.registration'),json={
            'wio':wio,
            'macaddress':macaddress,
            'code': code
        }
    )

def auth_wio(test_client,macaddress):
    return test_client.post(
        url_for('api.auth'),json={
            'macaddress':macaddress
        })

def get_access_token(test_client,macaddress):
    resp=auth_wio(test_client,macaddress)
    return resp.json['access_token']

"""
wios util
"""
def all_wio(test_client):
    return test_client.get(
        url_for('api.all')
    )

def find_wio(test_client,token):
    return test_client.get(
        url_for('api.find'), headers={"Authorization": f"Bearer {token}"}
    )

def delete_wio(test_client,token):
    return test_client.delete(
        url_for('api.delete'), headers={"Authorization": f"Bearer {token}"}
    )

def add_wio_data(test_client,token,type,value):
    return test_client.post(
        url_for('api.add_data'),json={
            'type':type,
            'value':value
        }, headers={"Authorization": f"Bearer {token}"}
    )

def view_wio_data(test_client,token):
    return test_client.get(
        url_for('api.view_data'), headers={"Authorization": f"Bearer {token}"}
    )

def view_wio_stats(test_client,token):
    return test_client.get(
        url_for('api.view_stats'), headers={"Authorization": f"Bearer {token}"}
    )
