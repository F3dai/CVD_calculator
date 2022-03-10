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

    assert data['ERROR'] == "['sex is not male or female']" 



"""
def test_bad_age():
    #Age out of range. Must be between 30 and 74
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '1', 'True', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert b"ERROR: age error." in response.data


def test_bad_smoker():
    response = test_client.get('/calculate', query_string=query_string_temp.format('male', '35', 'yes', '100', '100', '100'))
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert b"ERROR:" in response.data
    assert b"is not a boolean." in response.data



def test_bad_age_int():
    # check Age When A Non INT Is passed
    response1 = test_client.get('/calculate', query_string=query_string_temp.format('male', 'NotInteger', 'True', '100', '100', '100'))
    assert response1.status_code == 200
    assert b"ERROR:" in response1.data
    assert b"is not an integer." in response1.data


def test_bad_low_age_int():
    # check High / Low Age When An INT Is passed
    # accepted age range
    # >30 !=30
    # There is no max age 
    response2 = test_client.get('/calculate', query_string=query_string_temp.format('male', '29', 'True', '100', '100', '100'))
    assert response2.status_code == 200
    assert b"ERROR: age error." in response2.data


def test_bad_systolic_int():
    # check systolic When A Non INT Is passed
    response3 = test_client.get('/calculate', query_string=query_string_temp.format('male', '35', 'True', 'NotInteger', '100', '100'))    
    assert response3.status_code == 200
    assert b"ERROR:" in response3.data
    assert b"is not an integer." in response3.data


def test_bad_cholesterol_int():
   # check cholesterol When A Non INT Is passed
    response4 = test_client.get('/calculate', query_string=query_string_temp.format('male', '35', 'True', '100', 'NotInteger', '100'))
    assert response4.status_code == 200
    assert b"ERROR:" in response4.data
    assert b"is not an integer." in response4.data


def test_bad_hdl_int():
   # check hdl When A Non INT Is passed
    response5 = test_client.get('/calculate', query_string=query_string_temp.format('male', '35', 'True', '100', '100', 'NotInteger'))
    assert response5.status_code == 200
    assert b"ERROR:" in response5.data
    assert b"is not an integer." in response5.data


"""
