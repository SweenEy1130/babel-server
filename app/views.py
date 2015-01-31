from flask import render_template, request, session, redirect, url_for
from app import *
from app.model import User, Event
from decorator import *

@application.route('/signin', methods = ['GET'])
def Signin():
    return render_template('signin.html')

@application.route('/signin', methods = ['POST'])
def SigninResolve():
    try:
        usrn = request.form.get('username')
        if usrn and check_auth(usrn):
            session['username'] = request.form.get('username')
            __user = User.query.filter_by(username = session['username']).first()
            session['id'] = __user.id
            return redirect(url_for('Index'))
        else:
            return redirect(url_for('Signin'))
    except KeyError, e:
        return redirect(url_for('Signin'))

@application.route('/signout', methods = ['GET'])
def Signout():
    session.pop('username', None)
    return redirect(url_for('Signin'))

@application.route('/full', methods = ['GET'])
@requires_auth_html
def Full():
    return render_template('full.html')

@application.route('/index', methods = ['GET'])
@requires_auth_html
def Index():
    current_user = User.query.filter_by(username = session['username']).first()
    params = dict(current_user.serialize)
    return render_template('index.html', **params)

@application.route('/messages', methods = ['GET'])
@requires_auth_html
def Messages():
    current_user = User.query.filter_by(username = session['username']).first()

    return render_template('message.html')

@application.route('/events', methods = ['GET'])
@requires_auth_html
def Events():
 #get the data
        #action = int(request.form.get('action'))
        action = 1
        current_user = User.query.filter_by(username = session['username']).first()
        result = current_user.GetUserEvents(action)

    #return jsonify(result = current_user.GetUserEvents(action))
        return render_template('events.html', entries = result)

@application.route('/event/<int:eid>', methods = ['GET'])
@requires_auth_html
def ShowEventDetail(eid):
    __user = User.query.filter_by(username = session['username']).first()
    __event = Event.query.filter_by(id = eid).first()

    return render_template('event_detail.html', **dict(__event.serialize))

@application.route('/event_join/<int:eid>', methods = ['GET'])
@requires_auth_html
def JoinEvent(eid):
    __user = User.query.filter_by(username = session['username']).first()
    __event = Event.query.filter_by(id = eid).first()
    if __user in __event.applicants:
        return "You have duplicated application!"
    else:
        __event.applicants.append(__user)

    try:
        db.session.commit()
        return render_template('event_detail.html', **dict(__event.serialize))
    except SQLAlchemyError as e:
        return "%s"
    return render_template('event_detail.html', **dict(__event.serialize))
