# app.model
import datetime
from flask.ext.sqlalchemy import SQLAlchemy
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

    # owner lists
    owner_events = db.relationship('Event', secondary=owner_event_association,
        backref=db.backref('owner_event_association', lazy='dynamic'))

    # applicant lists
    applicant_events = db.relationship('Event', secondary=applicant_event_association,
        backref=db.backref('applicant_event_association', lazy='dynamic'))

    # participant lists
    participant_events = db.relationship('Event', secondary=participant_event_association,
        backref=db.backref('participant_event_association', lazy='dynamic'))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def serialize(self):
        owner_events = [item.description for item in self.owner_events]
        applicant_events = [item.description for item in self.applicant_events]
        participant_events = [item.description for item in self.participant_events]

        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'owner_events': owner_events,
            'applicant_events': applicant_events,
            'participant_events': participant_events
        }

class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(500))
    capacity = db.Column(db.Integer)
    available = db.Column(db.Integer)
    price = db.Column(db.String(30))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    owners = db.relationship('User', secondary = owner_event_association,
        backref=db.backref('owner_event_association', lazy='dynamic'))

    applicants = db.relationship('User', secondary = applicant_event_association,
        backref=db.backref('applicant_event_association', lazy='dynamic'))

    participants = db.relationship('User', secondary = participant_event_association,
        backref=db.backref('participant_event_association', lazy='dynamic'))

    def __init__(self, description, capacity, available, price):
        self.description = description
        self.capacity = capacity
        self.available = available
        self.price = price

    @property
    def serialize(self):
        owners = [item.username for item in self.owners]
        applicants = [item.username for item in self.applicants]
        participants = [item.username for item in self.participants]

        return {
            'description': self.description,
            'capacity': self.capacity,
            'available': self.available,
            'price': self.price,
            'create date': self.create_date,
            'owners': owners,
            'applicants': applicants,
            'participants': participants
        }
