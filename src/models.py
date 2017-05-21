from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from src.database import Base


class MeetupGroup(Base):
    __tablename__ = 'meetup_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    meetup_group_id = Column(String(80), unique=True)

    def __init__(self, name, meetup_group_id):
        self.name = name
        self.meetup_group_id = meetup_group_id


class TeamUpCalendar(Base):
    __tablename__ = 'teamup_calendar'
    id = Column(Integer, primary_key=True)
    team_group_id = Column(String(80), unique=True)
    meetup_group_id = Column(Integer, ForeignKey('meetup_group.id'),
                                unique=True)
    meetup_group = relationship(
            'MeetupGroup',
            backref=backref('meetup_group', uselist=False)
    )

    def __init__(self, team_group_id, meetup_group):
        self.team_group_id = team_group_id
        self.meetup_group = meetup_group
