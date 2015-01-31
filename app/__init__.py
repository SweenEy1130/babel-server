# app.__init__
from flask import Flask, Response, json
from app.model import *

application = Flask(__name__)
db.init_app(application)

# Register handlers
import app.helloworld
import app.login
