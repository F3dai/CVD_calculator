from cvd_app import create_app

def test_index_route():
    """
    GIVEN - / URL
    WHEN - User access application
    THEN - STATUS 200 - OK returned
    """
    app = create_app()
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200