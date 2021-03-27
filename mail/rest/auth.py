from flask import Flask, Blueprint, current_app, request, Markup, abort, render_template

app = Blueprint('auth', __name__)

@app.route('/logout')
def logout():
    return 'Logout'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')