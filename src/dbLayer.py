from src.settings import db


class MeetupGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meetup_group_id = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class TeamUpCalendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_group_id = db.Column(db.String(80), unique=True)
    meetup_group = db.relationship('MeetupGroup',
                                   backref=db.backref('team_up_calendar',
                                                      lazy='dynamic'))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
