from cvd_app import create_app
from flask import json

def test_ping_route():
    """
    GIVEN - /ping URL
    WHEN - User access application
    THEN - STATUS 200 - OK returned
    THEN - 
    {
      "message": "pong!", 
      "status": "Epic success"
    }
    """
    app = create_app()
    with app.test_client() as test_client:
        response = test_client.get('/ping')

        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert data['message'] == "pong!"
        assert data['status'] == "Epic success"


