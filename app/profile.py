# app.users

"""
API(Post):
    /create_user @parameter [username:zhangsan, password:123]
    /delete_user
    /edit_user  @parameter[Usernaem]
    /view_user userID[UserId]
    /accept_applicant

"""
import sys
from app import login
from app.model import *
from app import *
from flask import jsonify, request, session
from decorator import requires_auth

@application.route("/create_user", methods=['Get'])
def create_user():
    try:
        usrn = request.args.get('username')
        email = request.args.get('email')
        passwd = request.args.get('password')
        if  usrn and check_auth(usrn):
            return jsonify(results = {'WWW-Authenticate': 'User %s already exists' % usrn})
        else:
            newUser = User(usrn, email)
            db.session.add(newUser)
            db.session.commit();
            return jsonify(results = {'user':usrn, 'email':email, '':'item was created'})
            #write to the database
    except ValueError:
        sys.stderr.write('get user infor error!')

@application.route("/delete_user", methods=['Get'])
def delete_user():
    ##Todo
    usrn = request.args.get('username')
    user = User.query.filter_by(username = usrn).first()
    if user is None:
        return jsonify(results = {'WWW-Authenticate': 'User %s is not exist' % usrn})

    db.session.delete(user)
    db.session.commit()
    return jsonify(results = {'WWW-Authenticate': 'User %s deleted' % usrn})

@application.route("/edit_user", methods=['Get'])
@requires_auth
def edit_user():
    try:
        usrn = session['username']
        user = User.query.filter_by(username = usrn).first()

        status = request.args.get('status')
        description = request.args.get('description')
        user.status = status
        user.description = description

        session.submit()

    except ValueError:
        sys.stderr.write('get user information error!')

@application.route("/view_user", methods=['Get'])
@requires_auth
def view_user():
    try:
        usrn = request.args.get('username')
        user = User.query.filter_by(username = usrn).first()
        if user is None:
            return jsonify(results = {'Result':'user does not exist!'})
        else:
            return jsonify(results = user.serialize)
    except ValueError:
        sys.stderr.write('get user infor error!')

    #/create_user @parameter [username:zhangsan, password:123]
    #/delete_user
    #/edit_user  @parameter[Usernaem]
    #/view_user userID[UserId]
    #/accept_applicant

