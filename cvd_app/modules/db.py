from sqlalchemy import (
    create_engine, 
    Table, 
    MetaData,
    select,
    insert
)

class Database:

    # Just pass in Flask app object
    def __init__(self, app):
        self.app = app
        self.app.secret_key = b'1-#yC"!Fb80z\n\xec]/'

        username = "cvd_account"
        password = "james_charles00"
        host = "localhost"
        port = 3306
        database = "CVDCalculator"
        sql_arg = "" # "?auth_plugin=mysql_native_password"

        # Engine and db connection
        self.engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}{sql_arg}")
        self.conn = self.engine.connect()

        # Creating table classes
        self.accounts_table = Table('accounts', MetaData(), autoload=True, autoload_with=self.engine)
        self.records_table = Table('records', MetaData(), autoload=True, autoload_with=self.engine)


    def insert_record(self, data:dict):

        print(data)

        query = (
            insert(self.records_table).values({
                # There were some issues with passing data variable so just gonna hard code this shit instead for now
                    'sex': data["sex"], 
                    'age': int(data["age"]), 
                    'smoker': bool(data["smoker"]), 
                    'systolic': int(data["systolic"]), 
                    'cholesterol': int(data["cholesterol"]), 
                    'hdl': int(data["hdl"]), 
                    'birth_date': data["birth_date"], 
                    'nhs_id': int(data["nhs_id"]), 
                    'first_name': data["first_name"], 
                    'second_name': data["second_name"], 
                    'chd_risk': int(data["risk"])
                }
            )
        )
        
        self.conn.execute(query)

        return "Done"

    def check_account(self, email):

        query = select(self.accounts_table).where(self.accounts_table.c.email == email)
        result = self.conn.execute(query)
        result = result.mappings().all()[0]
        return result

    def show_profile(self, email):

        query = select(self.accounts_table).where(self.accounts_table.c.email == email)
        result = self.conn.execute(query)
        result = result.mappings().all()[0]
        return result

    def show_records(self):

        query = select(self.records_table)
        result = self.conn.execute(query)
        result = result.mappings().all()
        return result # Fetch one record and return res
