from flask import render_template
from app import *

@application.route('/signin', methods = ['GET'])
def Signin():
    return render_template('signin.html')

@application.route('/full', methods = ['GET'])
def Full():
    return render_template('full.html')

@application.route('/index', methods = ['GET'])
def Index():
    return render_template('index.html')

@application.route('/messages', methods = ['GET'])
def Messages():
    return render_template('message.html')

@application.route('/events', methods = ['GET'])
def Events():
    return render_template('events.html')

