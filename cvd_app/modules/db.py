import mysql.connector
import configparser

def establish():

    config = configparser.ConfigParser()

#    db = mysql.connector.connect(
#        host="localhost",
#        user="cvd_account",
#        password="james_charles00",
#        database="CVDCalculator"
#    )
    print(config.read('cvd_app/modules/mysql.cfg'))


    #print(type(config['MySQLCFG']['host']))

    print(config['MySQLCFG']['host'])
    print(config['MySQLCFG']['user'])
    print(config['MySQLCFG']['password'])
    print(config['MySQLCFG']['database'])


    try:
        dbconn = mysql.connector.connect(
           host=config['MySQLCFG']['host'],
           user=config['MySQLCFG']['user'],
           password=config['MySQLCFG']['password'],
           database=config['MySQLCFG']['database'],
            )


        if dbconn.is_connected():
            db_Info = dbconn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
    
            cursor = dbconn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            cursor.close()
            print("You're connected to database: ", record)
            return dbconn

    except Error as e:
        print("Error while connecting to MySQL", e)



def insert_record(data:dict, risk:int):


    db = establish()
    cursor = db.cursor()

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
    db.close()
    return f"{cursor.rowcount} change(s) made"
