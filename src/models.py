from src.settings import db


class MeetupGroup(db.Model):
    __tablename__ = 'meetup_group'
    id = db.Column(db.Integer, primary_key=True)
    meetup_group_id = db.Column(db.String(80), unique=True)

    def __init__(self, meetup_group_id):
        self.meetup_group_id = meetup_group_id


class TeamUpCalendar(db.Model):
    __tablename__ = 'teamup_calendar'
    id = db.Column(db.Integer, primary_key=True)
    team_group_id = db.Column(db.String(80), unique=True)
    meetup_group_id = db.Column(db.Integer, db.ForeignKey('meetup_group.id'),
                                unique=True)
    meetup_group = db.relationship(
            'MeetupGroup',
            backref=db.backref('meetup_group', uselist=False)
    )

    def __init__(self, team_group_id, meetup_group):
        self.team_group_id = team_group_id
        self.meetup_group = meetup_group
