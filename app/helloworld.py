# app.helloworld
"""
API:
    /initdb         test create User model
    /showdb         test list all the User
    /login?username=?
"""
from app.model import User
from app import *
from flask import jsonify, request, session
from decorator import requires_auth

@application.route("/initdb")
def InitDB():
    db.drop_all()
    db.create_all()
    admin = User('admin', 'admin@example.com')
    guest = User('guest', 'guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return 'OK'

@application.route("/showdb")
@requires_auth
def ShowDB():
    l = []
    for item in User.query.all():
        l.append(item.serialize)
    return jsonify(results = l)

from decorator import check_auth
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
