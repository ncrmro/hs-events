from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from src import settings

engine = create_engine(settings.DB_URL, convert_unicode=True)
db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))

Base = declarative_base()
Base.query = db.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from src.models import MeetupGroup, TeamUpCalendar
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures
    mup_group = MeetupGroup(name='SketchCity', meetup_group_id='1')
    db.add(mup_group)

    tup_calendar = TeamUpCalendar(team_group_id='1', meetup_group=mup_group)
    db.add(tup_calendar)
    db.commit()
