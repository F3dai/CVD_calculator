from flask import Flask,render_template,request,redirect
 
app = Flask(__name__)
 
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/calculate', methods = ['POST', 'GET'])
def calculate():
	if request.method == 'POST':
		return redirect("/")
	elif request.method == 'GET':
		return redirect("/")

app.run() # host='localhost', port=5000