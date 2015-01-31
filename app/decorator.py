from functools import wraps
from flask import Response, session, jsonify, redirect, url_for
from model import User

def check_auth(username):
    """This function is called to check if a username exists in database """
    return username and User.query.filter_by(username = username).first()

def not_authenticate():
    """Sends a 401 response that enables basic auth"""
    return jsonify(results = {'WWW-Authenticate': 'Login Required'}, status = 401)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'username' in session and check_auth(session['username']):
            return f(*args, **kwargs)
        else:
            return not_authenticate()
    return decorated

def requires_auth_html(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'username' in session and check_auth(session['username']):
            return f(*args, **kwargs)
        else:
            return redirect(url_for('Signin'))
    return decorated