
def test_confi(app):
    assert app.config['TESTING']==True