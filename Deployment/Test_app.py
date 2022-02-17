from flask import Flask, request, jsonify, render_template,send_from_directory
import pandas as pd
from Test_case import Test_project

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Test.html')

@app.route('/View',  methods=['POST'])
def View():
	desc = str(request.form['Desc'])
	app = str(request.form['App'])
	prio = str(request.form['Prio'])
	pred, pred_probability = Test_project(desc, app, prio)
	return render_template('Test.html', pred =pred, pred_probability=pred_probability)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)