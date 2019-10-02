import flask 
from flask import *
import pickle
import numpy 
app=flask.Flask(__name__)

@app.route('/')
def show_form():
	return render_template("iris.html")

@app.route('/predict',methods=['POST'])
def show_result():
	sepal_length=request.form['sepal_length']
	sepal_width=request.form['sepal_width']
	petal_length=request.form['petal_length']
	petal_width=request.form['petal_width']
	svc=pickle.load(open('svc.pkl','rb'))
	result=svc.predict([[sepal_length,sepal_width,petal_length,petal_width]])
	iris=['setosa', 'versicolor', 'virginica']
	return render_template("result.html",result=iris[result[0]])

if(__name__=="__main__"):
	app.run(debug = True)

