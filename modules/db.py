import mysql.connector

def establish():
    db = mysql.connector.connect(
        host="localhost",
        user="cvd_account",
        password="james_charles00",
        database="CVDCalculator"
    )
    return db


def insert_record(data:dict, risk:int):

    print(data)
    print(risk)


    db = establish()
    print(db)
    cursor = db.cursor()
    print(cursor)

    # Breakign somewhere here

    print("INSIDE")

    sql = ("INSERT INTO records (nhs_id, birth_date, sex, systolic, cholesterol, hdl, first_name, second_name, chd_risk) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    #add_employee = ("INSERT INTO employees (first_name, second_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)")
    
    print("SQL:", sql)


    nhs_id = data["nhs_id"]
    birth_date= data["birth_date"]
    sex = data["sex"]
    systolic = data["systolic"]
    cholesterol = data["cholesterol"]
    hdl = data["hdl"]
    first_name = data["first_name"]
    second_name = data["second_name"]
    risk = risk


    val = (nhs_id, birth_date, sex, systolic, cholesterol, hdl, first_name, second_name, risk)

    cursor.execute(sql, val)
    db.commit()

    return f"{cursor.rowcount} change(s) made"
