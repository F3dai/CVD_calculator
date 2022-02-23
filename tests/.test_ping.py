from cvd_app import create_app

def test_ping():
    """
    GIVEN - /ping URL
    WHEN - User access application
    THEN - STATUS 200 - OK returned
    """
    app = create_app()
    with create_app() as app:
        with flask_app.test_client() as test_client:
            response = app.test_client().get('/ping')
            assert response.status_code == 200
            #assert response.data.decode('utf-8') == 'Testing, Flask!'
