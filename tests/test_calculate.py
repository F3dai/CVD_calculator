from cvd_app import create_app
from flask import json

app = create_app()
test_client = app.test_client()
query_string_temp = 'sex={}&age={}&smoker={}&systolic={}&cholesterol={}&hdl={}'

def test_good_calculate():
    """
    GIVEN - /calculate?paramshere=1&params=2 URL
    WHEN - Calculate FUnctionality carried out
    THEN - STATUS 200 - 
    {
      "risk": 20
    }

    """
    #response = test_client.get('/calculate', query_string='sex={}&age={}&smoker={}&systolic={}&cholesterol={}&hdl={}&birth_date={}nhs_id{}&second_name={}&last{}'.format('male', '25', 'True', '100', '100', '100', '1977-06-08', '1234587900', 'kanye', 'west'))
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '25', 'True', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['risk'] == 20


def test_bad_sex():
    response = test_client.get('/calculate', query_string=query_string_temp.format('BAD', '25', 'True', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert b"ERROR:" in response.data
    assert b"is not a valid sex." in response.data


def test_bad_age():
    # low 13
    # high 110 ?

    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '1', '100', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))
    #Age out of range. Must be between 30 and 74



def test_bad_smoker():
    ...

def test_bad_systolic():
    ...

def test_bad_cholesterol():
    ...

def test_bad_hdl():
    ...

