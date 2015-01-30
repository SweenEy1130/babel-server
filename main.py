from flask import Flask
from settings import SECRET_KEY, PORT
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.secret_key = SECRET_KEY
    app.run(debug = True, port = PORT)