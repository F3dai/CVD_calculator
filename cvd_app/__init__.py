
from flask_bcrypt import Bcrypt
from flask import (
        Flask,
        render_template,
        request,
        redirect,
        jsonify,
        session,
        url_for
)


def create_app():
        """
        All API responses must be in this format:
        {
                "status" : "success | error",
                "message" : data
        }
        """
        app = Flask(__name__, template_folder='templates')
        from cvd_app.modules import db, faringdon_risk, faringdon_risk_v2#,risk

        bcrypt = Bcrypt(app)
        database = db.Database(app)

        @app.route('/', methods = ['GET'])
        def index():
                return render_template('index.html', authenticated=is_authenticated(session))

        # Return risk as %
        # Move this to another file??
        def get_risk(data:dict):
                # try:
                risk_obj = faringdon_risk.Calculate(
                        sex = data["sex"],
                        age = data["age"],
                        cholesterol = data["cholesterol"],
                        hdl = data["hdl"],
                        systolic = data["systolic"],
                        smoker = data["smoker"],
                        treatment = data["treatment"]                               
                )
                risk1 = risk_obj.calculate_risk()
                risk2 = faringdon_risk_v2.Calculate(
                        sex = data["sex"],
                        age = data["age"],
                        cholesterol = data["cholesterol"],
                        hdl = data["hdl"],
                        systolic = data["systolic"],
                        smoker = data["smoker"],
                        treatment = data["treatment"]                               
                ).calculate_risk()
                average = risk_obj.get_average()
                return {"status" : "successful", "message" : {"risk1" : risk1, "risk2": risk2, "average" : average}}
                # except Exception as response:
                #         return {"status" : "error", "message" : "ensure all fields are valid"}

        # Check if authentication is true in session
        def is_authenticated(session):
                if 'loggedin' in session:
                        return True
                else:
                        return False


        def checkem(data):
            # this function checks for data validation issues
            #print(data)

            errorlist = []
            params = [] 

            # 1 check all values are present
            # ImmutableMultiDict([('sex', 'male'), ('age', '75'), ('smoker', 'True'), ('systolic', '100'), ('cholesterol', '100'), ('hdl', '100')])
            if (data['sex'] and data['age'] and data['smoker'] and data['systolic'] and data['cholesterol'] and data['hdl']):
                print("All get params are there")
            else:
                for i in data:
                    print(data[i])
                    if not data[i]:
                        params.append(i)
                errorlist.append("Missing parameter[s]: " + str(params))
                kek =  {"ERROR": "" + str(errorlist)}
                return kek


            # check age is male or female 
            if not data['sex'] in ["male", "female"]:
                # value is not male or female
                errorlist.append("sex is not male or female")

            # check smoker is True or false
            if not (data['smoker'] == "True" or data['smoker'] == "False"):
                # value is not True or False for smoker status
                errorlist.append("smoking status is not True or False")

            # check age is an integer
            try:
                age = int(data['age'])
    
                if int(data['age']) < 30:
                    # too young
                    errorlist.append("age is too young")
            
                if int(data['age']) > 74:
                    # too old
                    errorlist.append("age is too old")
    
            except ValueError:
                errorlist.append("age is not an integer")

            # check systolic
            try:
                systolic = int(data['systolic'])
            except ValueError:
                errorlist.append("systolic is not an integer")

            # check cholesterol
            try:
                systolic = int(data['cholesterol'])
            except ValueError:
                errorlist.append("cholesterol is not an integer")

            # check hdl
            try:
                systolic = int(data['hdl'])
            except ValueError:
                errorlist.append("hdl is not an integer")


            ########## END HERE ##########
            if errorlist:
                #print({"ERROR": "" + str(errorlist)})
                kek =  {"ERROR": "" + str(errorlist)}
                #print(kek)
                return kek
            else:
                return "" # nice


        @app.route('/calculate', methods = ['POST', 'GET'])
        def calculate():
                # Submit data to database
                if request.method == 'POST':
                        risk = get_risk(request.form)
                        print(risk)
                        # Only insert if all these fields are present
                        if not request.form["nhs_id"] == "":
                                db_result = database.insert_record(request.form, risk["message"]["risk1"])
                                risk["message"]["result"] = db_result["status"]
                        else:
                                risk["message"]["result"] = "No data saved"
                        return risk

                # Just calculate
                elif request.method == 'GET':
                        # if checkem fails, return the output
                        # print("test")
                        # kek = checkem(request.args)
                        # print(kek)
                        # if "ERROR" in kek:
                        #     return kek
                        return get_risk(request.args)


        @app.route('/ping', methods=['GET'])
        def ping_pong():
           return jsonify(
                   {
                       'status': 'Epic success',
                       'message': 'pong!'
                   }
            )

        @app.route('/login', methods = ['POST', 'GET'])
        def login():
                msg = ''
                if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
                        # Create variables for easy access
                        email = request.form['email']
                        password_raw = request.form['password']

                        account = database.check_account(email) # account as dict

                        if bcrypt.check_password_hash(account["password"], password_raw):
                                # Create session data, we can access this data in other routes
                                session['loggedin'] = True
                                session['email'] = account['email']
                                # Redirect to logged in profile
                                return redirect(url_for('profile'))
                        else:
                                # Account doesnt exist or username/password incorrect
                                msg = 'No account or bad password reeee'

                # Output message if something goes wrong...
                return render_template('login.html', response=msg, authenticated=is_authenticated(session))


        @app.route('/logout')
        def logout():
                # Remove session data, this will log the user out
                session.pop('loggedin', None)
                session.pop('id', None)
                session.pop('email', None)
                # Redirect to login page
                return redirect(url_for('login'))


        @app.route('/profile')
        def profile():
                if is_authenticated(session):
                        res:dict = database.show_profile(session['email'])
                        return render_template('profile.html', data=res, authenticated=is_authenticated(session))
                else:
                        return redirect(url_for('login'))
        
        @app.route('/records')
        def records():
                if is_authenticated(session):
                        res:dict = database.show_records()
                        return render_template('records.html', records=res, authenticated=is_authenticated(session))
                else:
                        return redirect(url_for('login'))
        

        @app.route('/stats')
        def stats():
                if is_authenticated(session):
                        res:dict = database.show_records()
                        return render_template('stats.html', authenticated=is_authenticated(session))
                else:
                        return redirect(url_for('login'))


        return app
