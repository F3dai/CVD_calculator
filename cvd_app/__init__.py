from flask import Flask,render_template,request,redirect,jsonify,abort 

def create_app():
    app = Flask(__name__,template_folder='templates')
    from cvd_app.modules import risk, db

    @app.route('/', methods = ['GET'])
    def index():
        return render_template('index.html')

    # Return risk as %
    def get_risk(data:dict):
            try:
                    return risk.calculate(
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
                   res = db.insert_record(request.form, risk)
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
 
    return app
