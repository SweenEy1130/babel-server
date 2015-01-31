# app.helloworld
"""
API:
    /initdb         test create User model
    /showdb         test list all the User
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
    adams = User('adams', 'admas@example.com','1','11')
    bob = User('bob', 'bob@example.com','2','22')
    celia = User('celia', 'celia@example.com','3','33')
    david = User('david', 'david@example.com','4','44')
    # title, description, capacity, available, price, location, destination, event_date
    latrip = Event('LAtrip', 'Go around Los Angeles', 5, 4, '>500', 'USC North Campus', '99 Ranch', '11/30/1991 10:20:12')
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

