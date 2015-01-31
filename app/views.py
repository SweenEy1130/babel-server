from flask import render_template
from app import *

@application.route('/')
def index():
    return render_template('index.html')