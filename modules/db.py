import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb.cursors

# Some of these functions can def be reduced:
# just change sql query for each func then execute in seperate funcn


## Dont need this anymore - replaced by MySQL(app)
# def establish():
#     db = mysql.connector.connect(
#         host="localhost",
#         user="cvd_account",
#         password="james_charles00",
#         database="CVDCalculator"
#     )
#     return db

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


    def insert_record(self, data:dict, risk:int):

        sql = """INSERT INTO records (nhs_id, birth_date, sex, systolic, cholesterol, hdl, first_name, second_name, chd_risk) 
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

    def check_account(self, email, password):
        # db = establish()
        # cursor = db.cursor(dictionary=True)

        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = "SELECT * FROM accounts WHERE email = %s AND password = %s"
        val = (email, password)

        cursor.execute(sql, val)

        account = cursor.fetchone()
        return account 

    def show_profile(self, email):
        # db = establish()
        # cursor = db.cursor()

        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = "SELECT * FROM accounts WHERE email = %s"
        val = (email,)

        cursor.execute(sql, val)

        return cursor.fetchone() # Fetch one record and return res