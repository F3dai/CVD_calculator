# cvd_app/modules/db.py

import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb.cursors
import configparser

class Database:

    # Just pass in Flask app object
    def __init__(self, app):
        self.app = app
        configpars = configparser.ConfigParser()
        self.mysql = MySQL(self.app)
        configpars.read('cvd_app/modules/mysql.cfg')
        self.app.secret_key                       = b'1-#yC"!Fb80z\n\xec]/'
        self.app.config['MYSQL_HOST']     = configpars['MySQLCFG']['host']
        self.app.config['MYSQL_USER']     = configpars['MySQLCFG']['user']
        self.app.config['MYSQL_PASSWORD'] = configpars['MySQLCFG']['password']
        self.app.config['MYSQL_DB']       = configpars['MySQLCFG']['database']


    def insert_record(self, data:dict, risk:int):
        
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

        # gogogogo working
        cursor = self.mysql.connection.cursor()
        cursor.execute(sql, val)
        self.mysql.connection.commit()
        cursor.close()


        return f"{cursor.rowcount} change(s) made"


    def check_account(self, email, password):
        # db = establish()
        # cursor = db.cursor(dictionary=True)

        sql = "SELECT * FROM accounts WHERE email = %s AND password = %s"
        val = (email, password)

        cursor = self.mysql.connection.cursor()
        cursor.execute(sql, val)
        self.mysql.connection.commit()
        account = cursor.fetchone()
        cursor.close()

        return account 

    def show_profile(self, email):
        # db = establish()
        # cursor = db.cursor()

        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = "SELECT * FROM accounts WHERE email = %s"
        val = (email,)

        cursor = self.mysql.connection.cursor()
        cursor.execute(sql, val)
        self.mysql.connection.commit()
        account = cursor.fetchone()
        cursor.close()
        return account 
