#!/usr/bin/python3

from flask import Flask,request,render_template,url_for
import requests
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
	if request.method =='GET':
		return render_template('index.html')
	elif request.method == "POST":
		url = request.form['url']
		cuttly = "https://cutt.ly/scripts/shortenUrl.php"
		data = {"url":url}
		short = requests.post(cuttly,data=data).text
		hasil = short
		
		return render_template('index.html',hasil=hasil)
		
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80,debug=True)


