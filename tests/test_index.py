from cvd_app import create_app

def test_index_route():

    app = create_app()
    
    response = app.test_client().get('/')

    assert response.status_code == 200
    #assert response.data.decode('utf-8') == 'Testing, Flask!'
