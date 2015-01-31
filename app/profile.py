# app.users

"""
POST    /create_user @parameter [username:zhangsan, password:123]
POST    /delete_user
POST    /edit_user  @parameter[Usernaem]
POST    /view_user userID[UserId]
POST    /accept_applicant

"""
import sys
from app.model import *
from app import *
from flask import jsonify, request, session
from decorator import requires_auth
from sqlalchemy.exc import SQLAlchemyError

@application.route("/create_user", methods=['POST'])
def create_user():
    try:
        usrn = request.form.get('username')
        email = request.form.get('email')
        passwd = request.form.get('password')
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

@application.route("/delete_user", methods=['POST'])
def delete_user():
    ##Todo
    usrn = request.form.get('username')
    user = User.query.filter_by(username = usrn).first()
    if user is None:
        return jsonify(results = {'WWW-Authenticate': 'User %s is not exist' % usrn})

    db.session.delete(user)
    db.session.commit()
    return jsonify(results = {'WWW-Authenticate': 'User %s deleted' % usrn})

@application.route("/edit_user", methods=['POST'])
@requires_auth
def edit_user():
    try:
        usrn = session['username']
        user = User.query.filter_by(username = usrn).first()

        status = request.form.get('status')
        description = request.form.get('description')
        user.status = status
        user.description = description


        try:
            db.session.commit()
            return jsonify(status = 0)
        except SQLAlchemyError as e:
            return jsonify(status = -1, info = "%s" % str(e))
    except ValueError:
        sys.stderr.write('get user information error!')

@application.route("/view_user", methods=['POST'])
@requires_auth
def view_user():
    try:
        usrn = request.form.get('username')
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
