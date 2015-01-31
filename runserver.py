# runserver

from app import application
from config import *

if __name__ == "__main__":
    application.config.from_object(__name__)
    application.run(port = PORT, host = HOST)