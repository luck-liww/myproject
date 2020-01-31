#!/use/bin/python
# -*- coding:utf-8 -*-

from flask import Flask,render_template,url_for,Response,redirect,abort,json
from flask_script import Manager
import uuid

app = Flask(__name__)
manager = Manager(app=app)

@app.route('/')
def hello_world():
	return 'hello,World!'

@app.route('/hello/')
def hello1():
	print("1111")
	return render_template('hello.html')

@app.route('/params/<hehe>/')
def params(hehe):
	print(hehe)
	return '打印参数'

@app.route('/getuuid/<uuid:name>/')
def get_uuid(name):
	print(name)
	return '打印参数'

@app.route('/respuuid/')
def resp_uuid():
	return str(uuid.uuid4())

@app.route('/url/')
def url():
	print(url_for('resp_uuid'))
	return '反向解析'

@app.route('/response/')
def resp():
	result = render_template('hello.html')
	# print(result)
	# print(type(result))
	response = Response(response = '<h2>德玛西亚</h2>',status = 403)

	return response

@app.route('/redirect/')
def redi():

	return redirect(url_for('resp'))

@app.route('/abort/')
def ab():

	abort(403)

@app.route('/json/')
def js():

	# result = json.jsonify({'name':'value'})
	# result = json.jsonify(name='value',age=18)
	result = json.jsonify({'name':'value','age': 18})

	return result

if __name__ == '__main__':
	manager.run()
