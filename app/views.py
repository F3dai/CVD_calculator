from app import app 
from flask import Flask,render_template,request,redirect,jsonify,abort

from app.modules import risk, db

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
                # abort(400, "wrong input")


@app.route('/calculate', methods = ['POST', 'GET'])
def calculate():
        # Submit data to database
        if request.method == 'POST':
                print(request.form)
                risk = get_risk(request.form)["risk"]
                print("RISK:", risk)
                print("REQ:", request.form)
                res = db.insert_record(request.form, risk)

                print("RES:", res)
                return jsonify(res)

        # Just calculate
        elif request.method == 'GET':
                risk = get_risk(request.args)

                print("request.args", request.args)
                print("risk", risk)
                return jsonify(risk)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify(
            {
                'status': 'Epic success',
                'message': 'pong!'
            }
    )
