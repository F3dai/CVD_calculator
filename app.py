from flask import Flask,render_template,request,redirect,jsonify
 
app = Flask(__name__)
 
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/calculate', methods = ['POST', 'GET'])
def calculate():
	if request.method == 'POST':
		return jsonify({"result" : "POST request works!"})
	elif request.method == 'GET':
		data = dict(request.args)
		
		return jsonify(data)

app.run() # host='localhost', port=5000