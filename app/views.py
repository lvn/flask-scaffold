from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from app import app, db, lm
# from models import

# View functions go here.
@app.route('/')
def index():
	return render_template('index.html')