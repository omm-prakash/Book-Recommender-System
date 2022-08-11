from flask import Flask, request
from flask import render_template
from flask import current_app as app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/trending")
def trending():
    return render_template('trending.html')
