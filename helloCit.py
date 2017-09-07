import os
import cPickle as pickle
import sqlite3
from flask import Flask

app=Flask(_name_)
app.debug=True
app.secret_key="122"
authenticated=True
isAdmin=False

@app.route("/")
def index():
	return "Welcome"
	

@app.route("/login")
def login (uname,passwd):
	conn=sqlite3.connect('app.db')
	cur=conn.execute('select username,password from Users where name='%s'" %uname)
	if uname==admin" || passwd==cur[1]:
		isAdmin=True
		authenticated=True
		print "welcome" + uname
	elif uname == cur[0] && passwd==cur[1]:
		isAdmin=False
		authenticated=True
		print "Welcome"+uname
	else:
		isAdmin=False
		authenticated=False
		print"incorect"
		

@app.route("/cmd")
def do(data,cmd):
	if isAdmin && cmd== "cat":
		d= pickle.load(data)
		cmd="cat"
		cmd += d['file']
		out=subprocess.call(cmd,shell=True)
		print out
	elif authenticated and cmd=="ping":
		d=pickle.load(data)
		cmd="ping -c 1"
		cmd += d['ip']
		out=subprocess.call(cmd,shell=True)
		print out
