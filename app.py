from flask import Flask,render_template,request,redirect,jsonify,abort
from modules import risk, db
 
app = Flask(__name__)


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
		return jsonify(str(response))
		# abort(400, "wrong input")	


@app.route('/calculate', methods = ['POST', 'GET'])
def calculate():
	# Submit data to database
	if request.method == 'POST':
		print(request.form)
		risk = get_risk(request.form)["risk"]
		res = db.insert_record(request.form, risk)
		print(res)
		return jsonify(res)

	# Just calculate
	elif request.method == 'GET':
		risk = get_risk(request.args)
		return jsonify(risk)


if __name__ == "__main__":
	app.run() # host='localhost', port=5000