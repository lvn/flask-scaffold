from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from app import app, db, lm
# from models import

# View functions go here.
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
	if (request.method == 'POST'):
		# register new account models
		return
	return render_template('register.html', title="Register your account")

@app.route('/login/', methods=['GET','POST'])
def login():
	if (request.method == 'POST'):
		# login account
		return
	return render_template('login.html', title="Login")