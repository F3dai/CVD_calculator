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
    db = establish()
    cursor = db.cursor()

    # Breakign somewhere here

    sql = f"""INSERT INTO records (nhs_id, birth_date, sex, systolic, cholesterol, hdl, first_name, second_name, chd_risk) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    val = (
        data["nhs_id"],
        data["birth_date"],
        data["sex"],
        data["systolic"],
        data["cholesterol"],
        data["hdl"],
        data["first_name"],
        data["second_name"],
        risk
    ) # Convert dict to tuple of values
    
    cursor.execute(sql, val)
    db.commit()

    return f"{cursor.rowcount} change(s) made"
