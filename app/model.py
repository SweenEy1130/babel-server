# app.model
import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from app.utils import escapeDatetime

db = SQLAlchemy()

owner_event_association = db.Table('owner_event_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

applicant_event_association = db.Table('applicant_event_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

participant_event_association = db.Table('participant_event_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20), default='')
    status = db.Column(db.String(50), default='')
    description = db.Column(db.String(500), default='')

    # owner lists
    owner_events = db.relationship('Event', secondary=owner_event_association)
    # applicant lists
    applicant_events = db.relationship('Event', secondary=applicant_event_association)
    # participant lists
    participant_events = db.relationship('Event', secondary=participant_event_association)

    def GetUserEvents(self, action):
        if action == 1:
            return [item.serialize for item in self.owner_events]
        elif action == 2:
            return [item.serialize for item in self.applicant_events]
        elif action == 3:
            return [item.serialize for item in self.participant_events]
        else:
            return [item.serialize for item in list(set(self.owner_events) | set(self.applicant_events) | set(self.participant_events))]

    def __init__(self, username, email, status = '', description = ''):
        self.username = username
        self.email = email
        self.status = status
        self.description = description

    @property
    def serialize(self):
        owner_events = [item.title for item in self.owner_events]
        applicant_events = [item.title for item in self.applicant_events]
        participant_events = [item.title for item in self.participant_events]

        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'status': self.status,
            'description': self.description,
            'owner_events': owner_events,
            'applicant_events': applicant_events,
            'participant_events': participant_events,
            'id':self.id
        }

class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(500))
    capacity = db.Column(db.Integer)
    available = db.Column(db.Integer)
    price = db.Column(db.String(30))
    location = db.Column(db.String(30))
    destination = db.Column(db.String(50))
    event_date = db.Column(db.DateTime, default=datetime.datetime.now)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    owners = db.relationship('User', secondary = owner_event_association)
    applicants = db.relationship('User', secondary = applicant_event_association)
    participants = db.relationship('User', secondary = participant_event_association)

    def __init__(self, title, description, capacity, available, price, location, destination, event_date):
        self.title = title
        self.description = description
        self.capacity = capacity
        self.available = available
        self.price = price
        self.location = location
        self.destination = destination
        self.event_date = escapeDatetime(event_date)

    @property
    def serialize(self):
        owners = [item.username for item in self.owners]
        applicants = [item.username for item in self.applicants]
        participants = [item.username for item in self.participants]

        return {
            'title': self.title,
            'description': self.description,
            'capacity': self.capacity,
            'available': self.available,
            'price': self.price,
            'location': self.location,
            'destination': self.destination,
            'event date': self.event_date,
            'create date': self.create_date,
            'owners': owners,
            'applicants': applicants,
            'participants': participants,
            'id': self.id
        }
