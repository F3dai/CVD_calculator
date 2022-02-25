# cvd_app/__init__.py


from flask import (
        Flask,
        render_template,
        request,
        redirect,
        jsonify,
        abort,
        session,
        url_for
)

def create_app():
    app = Flask(__name__,template_folder='templates')

    from cvd_app.modules import risk, db

    #changed
    database = db.Database(app)
    #changed

    @app.route('/', methods = ['GET'])
    def index():
        return render_template('index.html')

    # Return risk as %
    def get_risk(data:dict):
            try:
                    return risk.Calculate(
                            sex = data["sex"],
                            age = data["age"],
                            smoker = data["smoker"],
                            systolic = data["systolic"],
                            cholesterol = data["cholesterol"],
                            hdl = data["hdl"]
                    ).calculate_risk()
    
            except Exception as response:
                    print("EXCEPTION:", str(response))
                    return str(response)
            #        # abort(400, "wrong input")
    
    
    @app.route('/calculate', methods = ['POST', 'GET'])
    def calculate():
           # Submit data to database
           if request.method == 'POST':

                   risk = get_risk(request.form)["risk"]
                   res = database.insert_record(request.form, risk)
                   return jsonify(res)
    
           # Just calculate
           elif request.method == 'GET':
                   risk = get_risk(request.args)
    
                   #print("request.args", request.args)
                   #print("risk", risk)
                   return jsonify(risk)
    

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
                    email = request.form['email']
                    password = request.form['password']
                    account = database.check_account(email, password)
    
                    if account:
                            # Create session data, we can access this data in other routes
                            session['loggedin'] = True
                            session['email'] = account[3] # 'email', cant use str index in tuple
                            # Redirect to home page

                            print("GOOD ACCOUNT")
                            return redirect(url_for('profile'))
                    else:
                            # Account doesnt exist or username/password incorrect
                            msg = 'No account or bad password reeee'
                            print(msg)
    
            # Output message if something goes wrong...
            return render_template('login.html', response=msg)


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
        if 'loggedin' in session:
                res:dict = database.show_profile(session['email'])
                return render_template('profile.html', data=res)
        else:
                return redirect(url_for('login'))


    return app
