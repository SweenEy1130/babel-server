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
# @requires_auth
def InitDB():
    db.drop_all()
    db.create_all()
    adams = User('adams', 'admas@example.com')
    bob = User('bob', 'bob@example.com')
    celia = User('celia', 'celia@example.com')
    david = User('david', 'david@example.com')
    latrip = Event('LAtrip', 5, 4, 0)
    latrip.owners.append(adams)
    latrip.applicants.append(david)
    latrip.applicants.append(bob)
    latrip.participants.append(adams)
    latrip.participants.append(celia)
    db.session.add(adams)
    db.session.add(bob)
    db.session.add(celia)
    db.session.add(david)
    db.session.add(latrip)
    db.session.commit()
    return 'OK'

@application.route("/listdb")
def ShowDB():
    l = [item.serialize for item in User.query.all()]
    e = [item.serialize for item in Event.query.all()]
    return jsonify(user = l, event = e)

