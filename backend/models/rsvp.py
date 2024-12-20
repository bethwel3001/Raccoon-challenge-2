from . import db

class RSVP(db.Model):
    __tablename__ = 'rsvps'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # e.g., 'Confirmed', 'Pending'

    user = db.relationship('User', backref='rsvps', lazy=True)
    event = db.relationship('Event', backref='rsvps', lazy=True)
