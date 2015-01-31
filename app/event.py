# app.event
from app.model import User, Event
from app import *
from flask import jsonify, request, session
from sqlalchemy.exc import SQLAlchemyError
from decorator import requires_auth

"""
API documentation for Events
POST    /get_event_list
        @parameter:
            action: Int
                1 for owned events
                2 for applied events
                3 for participated events
                4 for all events relating to me
        @response:
            result: model.Event JSON
"""
@application.route("/get_event_list",  methods=['POST'])
@requires_auth
def GetEventList():
    action = int(request.form.get('action'))
    current_user = User.query.filter_by(username = session['username']).first()
    return jsonify(result = current_user.GetUserEvents(action))


"""
POST    /create_event
        @parameter:
            description: String
            capacity: Int
            available: Int
            price: String
            location: String
        @response:
            status: 0  for success
                    -1 for error
"""
@application.route("/create_event", methods=['POST'])
@requires_auth
def CreateEvent():
    current_user = User.query.filter_by(username = session['username']).first()
    title = request.form.get('title')
    description = request.form.get('description')
    capacity = request.form.get('capacity')
    available = request.form.get('available')
    price = request.form.get('price')
    location = request.form.get('location')
    destination = request.form.get('destination')
    event_date = request.form.get('event_date')

    new_event = Event(title, description, capacity, available, price, location, destination, event_date)
    new_event.owners.append(current_user)
    new_event.participants.append(current_user)
    db.session.add(new_event)
    try:
        db.session.commit()
        return jsonify(status = 0)
    except SQLAlchemyError as e:
        return jsonify(status = -1, info = "%s" % str(e))

"""
POST    /edit_event
        @parameter:
            eid: Int
            description: String
            capacity: Int
            available: Int
            price: String
            location: String
        @response:
            status: 0  for success
                    -1 for error
"""
from app.utils import escapeDatetime
@application.route("/edit_event", methods=['POST'])
@requires_auth
def EditEvent():
    current_user = User.query.filter_by(username = session['username']).first()
    eid = request.form.get('eid')
    title = request.form.get('title')
    description = request.form.get('description')
    capacity = request.form.get('capacity')
    available = request.form.get('available')
    price = request.form.get('price')
    location = request.form.get('location')
    destination = request.form.get('destination')
    event_date = request.form.get('event_date')

    old_event = Event.query.filter_by(id = eid).first()
    old_event.title = title
    old_event.description = description
    old_event.capacity = capacity
    old_event.available = available
    old_event.price = price
    old_event.location = location
    old_event.destination = destination
    old_event.event_date = escapeDatetime(event_date)

    try:
        db.session.commit()
        return jsonify(status = 0)
    except SQLAlchemyError as e:
        return jsonify(status = -1, info = "%s" % str(e))

"""
POST    /delete_event
        @parameter:
            eid: Int
        @response:
            status: 0  for success
                    -1 for error
"""
@application.route("/delete_event", methods=['POST'])
@requires_auth
def DeleteEvent():
    current_user = User.query.filter_by(username = session['username']).first()
    eid = request.form.get('eid')

    delete_event = Event.query.filter_by(id = eid).first()
    if not delete_event:
        return jsonify(status = -2, info = "Events doesn't exist")
    try:
        db.session.delete(delete_event)
        db.session.commit()
        return jsonify(status = 0)
    except SQLAlchemyError as e:
        return jsonify(status = -1, info = "%s" % str(e))

"""
POST    /apply_event
@parameter:
    eid: Int
@response:
status:
    0 for success
    -1 for
    -2 for duplicated application
"""
@application.route("/apply_event", methods=['POST'])
@requires_auth
def ApplyEvent():
    current_user = User.query.filter_by(username = session['username']).first()
    eid = request.form.get('eid')

    apply_event = Event.query.filter_by(id = eid).first()
    if current_user in apply_event.applicants:
        return jsonify(status = -2, info = "You have duplicated application!")
    else:

        apply_event.applicants.append(current_user)

    try:
        db.session.commit()
        return jsonify(status = 0)
    except SQLAlchemyError as e:
        return jsonify(status = -1, info = "%s" % str(e))

"""
POST    /approve_apply
@parameter:
    eid: Int
    uid: Int
@response:
    status:
        0 for success
        -1 for already approved
        -2 for not authorized
        -3 for not an applicants
        -4 for user doesn't exists
        -5 for SQL error
"""
@application.route("/approve_apply", methods=['POST'])
@requires_auth
def ApproveApplication():
    current_user = User.query.filter_by(username = session['username']).first()
    eid = request.form.get('eid')
    uid = request.form.get('uid')

    apply_event = Event.query.filter_by(id = eid).first()
    apply_user = User.query.filter_by(id = uid).first()

    if not apply_user:
        return jsonify(status = -4, info = "User doesn't exist!")

    if current_user not in apply_event.owners:
        return jsonify(status = -2, info = "You have permmision to approve participants!")
    if apply_user not in apply_event.applicants:
        return jsonify(status = -3, info = "The user doesn't submit the application!")
    elif apply_user in apply_event.participants:
        return jsonify(status = -1, info = "The user has already been in the participants list!")
    else:
        apply_event.participants.append(apply_user)
        apply_event.applicants.remove(apply_user)

    try:
        db.session.commit()
        return jsonify(status = 0)
    except SQLAlchemyError as e:
        return jsonify(status = -5, info = "%s" % str(e))
