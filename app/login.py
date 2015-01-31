# app.login
"""
API:
    /login?username=adams&password=123      Login API
    /logout                                 Logout API
"""
from app.model import User
from app import *
from flask import jsonify, request, session
from decorator import requires_auth, check_auth

@application.route("/login",  methods=['GET'])
def Login():
    try:
        usrn = request.args.get('username')
        if  usrn and check_auth(usrn):
            session['username'] = request.args.get('username')
        else:
            return jsonify(results = {'WWW-Authenticate': 'User %s doesn\'t exists' % usrn})
    except KeyError, e:
        print 'I got a KeyError - reason "%s"' % str(e)
    return jsonify(results = {'WWW-Authenticate': 'Login success as %s' % session['username']})

@application.route("/logout", methods=['GET'])
def Logout():
    session.pop('username', None)
    return jsonify(results = {'WWW-Authenticate': 'Logout success'})