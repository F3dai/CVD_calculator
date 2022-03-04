from cvd_app.modules import risk, db
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
	app = Flask(__name__, template_folder='templates')
	database = db.Database(app)

	@app.route('/', methods = ['GET'])
	def index():
		return render_template('index.html')

	# Return risk as %
	# Move this to another file??
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
			return jsonify(str(response))
			# abort(400, "wrong input")	


	@app.route('/calculate', methods = ['POST', 'GET'])
	def calculate():
		# Submit data to database
		if request.method == 'POST':
			print(request.form)
			risk = get_risk(request.form)["risk"]
			res = database.insert_record(request.form, risk)
			print(res)
			return jsonify(res)

		# Just calculate
		elif request.method == 'GET':
			risk = get_risk(request.args)
			return jsonify(risk)


	@app.route('/login', methods = ['POST', 'GET'])
	def login():
		msg = ''
		if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
			# Create variables for easy access
			email = request.form['email']
			password = request.form['password']
			print(email, password)
			account = database.check_account(email, password)

			print(account)

			if account:
				# Create session data, we can access this data in other routes
				session['loggedin'] = True
				session['email'] = account['email']
				# Redirect to home page
				return redirect(url_for('profile'))
			else:
				# Account doesnt exist or username/password incorrect
				msg = 'No account or bad password reeee'

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