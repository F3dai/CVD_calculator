from cvd_app import create_app
from flask import json

app = create_app()
test_client = app.test_client()
query_string_temp = 'sex={}&age={}&smoker={}&systolic={}&cholesterol={}&hdl={}'

def test_good_calculate():
    #response = test_client.get('/calculate', query_string='sex={}&age={}&smoker={}&systolic={}&cholesterol={}&hdl={}&birth_date={}nhs_id{}&second_name={}&last{}'.format('male', '25', 'True', '100', '100', '100', '1977-06-08', '1234587900', 'kanye', 'west'))
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '35', 'True', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))
    print(data)

    assert response.status_code == 200
    assert data['risk'] == 20


def test_bad_sex():
    response = test_client.get('/calculate', query_string=query_string_temp.format('BAD', '35', 'True', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['ERROR']
    assert 'sex is not male or female' in data['ERROR']


def test_bad_age_low():
    #Age out of range. Must be between 30 and 74
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '1', 'True', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['ERROR']
    assert 'age is too young' in data['ERROR']


def test_bad_age_high():
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '85', 'True', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['ERROR']
    assert 'age is too old' in data['ERROR']

def test_bad_smoker():
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '35', 'yes', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['ERROR']
    assert 'smoking status is not True or False' in data['ERROR']


def test_bad_age_int():
    # check Age When A Non INT Is passed
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', 'NotInteger', 'True', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['ERROR']
    assert 'age is not an integer' in data['ERROR']  


def test_bad_systolic_int():
    # check systolic When A Non INT Is passed
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '35', 'True', 'NotInteger', '100', '100'))    
    
    data = json.loads(response.get_data(as_text=True))
 
    assert response.status_code == 200
    assert data['ERROR']
    assert 'systolic is not an integer' in data['ERROR']

def test_bad_cholesterol_int():
   # check cholesterol When A Non INT Is passed
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '35', 'True', '100', 'NotInteger', '100'))
    
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['ERROR']
    assert 'cholesterol is not an integer' in data['ERROR']

def test_bad_hdl_int():
   # check hdl When A Non INT Is passed
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '35', 'True', '100', '100', 'NotInteger'))
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['ERROR']
    assert 'hdl is not an integer' in data['ERROR']

