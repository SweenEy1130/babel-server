# app.login
"""
API:
POST    /login                    Login API
    @parameter
    - username: String
    - password: String
POST    /logout                   Logout API
"""
from app.model import User
from app import *
from flask import jsonify, request, session
from decorator import requires_auth, check_auth

@application.route("/login",  methods=['POST','GET'])
def Login():
    try:
        usrn = request.form.get('username')
        if usrn and check_auth(usrn):
            session['username'] = request.form.get('username')
        else:
            return jsonify(status = -1, info = 'User does not exist')
    except KeyError, e:
        return jsonify(status = -2, info = 'I got a KeyError - reason "%s"' % str(e))

    return jsonify(status = 0)

@application.route("/logout", methods=['POST'])
def Logout():
    session.pop('username', None)
    return jsonify(status = 0)