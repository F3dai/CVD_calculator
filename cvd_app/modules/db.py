import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb.cursors

# Some of these functions can def be reduced:
# just change sql query for each func then execute in seperate func

class Database:

    # Just pass in Flask app object
    def __init__(self, app):
        self.app = app

        self.mysql = MySQL(self.app)
        self.app.secret_key = b'1-#yC"!Fb80z\n\xec]/'
        self.app.config['MYSQL_HOST'] = 'localhost'
        self.app.config['MYSQL_USER'] = 'cvd_account'
        self.app.config['MYSQL_PASSWORD'] = 'james_charles00'
        self.app.config['MYSQL_DB'] = 'CVDCalculator'

        # Indexes for converting points to values 
        self.age = ["20-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79"]
        self.sex = ["male", "female"]
        self.cholesterol = [">160","160-199","200-239","240-279","<=280"]
        self.hdl = [">=60","50-59","40-49",">40"]
        self.systolic = [">;120","120-129","130-139","140-159","<=160"]
        self.smoker = [False, True]
        self.pressure = [False, True]

    
    def execute(self, sql, val=None, action="fetchone"):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sql, val)
        self.mysql.connection.commit()

        if action == "fetchone":
            return cursor.fetchone()
        elif action == "rowcount":
            return cursor.rowcount
        elif action == "fetchall":
            return cursor.fetchall()
        else:
            return {"error": f"unrecognised action: {action}. This is backend issue"}


    def insert_record(self, data:dict, risk:int):
        sql = """INSERT INTO records (nhs_id, birth_date, age, smoker, sex, systolic, cholesterol, hdl, first_name, second_name, chd_risk) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val =( 
            data["nhs_id"],
            data["birth_date"],
            self.age[int(data["age"])],
            bool(data["smoker"]),
            self.sex[int(data["sex"])],
            self.systolic[int(data["systolic"])],
            self.cholesterol[int(data["cholesterol"])],
            self.hdl[int(data["hdl"])],
            data["first_name"],
            data["second_name"],
            risk
        )
        
        self.execute(sql, val, action="rowcount")
        return {"status" : "successful", "message" : {}}

    def check_account(self, email):
        sql = '''SELECT * FROM accounts WHERE email = %s'''
        val = (email,)
        result = self.execute(sql, val)
        return result 


    def show_profile(self, email):
        sql = "SELECT * FROM accounts WHERE email = %s"
        val = (email,)
        result = self.execute(sql, val)
        return result

    def show_records(self):
        query = "SELECT * FROM records"
        result = self.execute(query, action="fetchall")
        return result # Fetch one record and return res
