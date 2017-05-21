from src import app, db, models, MeetupAdapterClient, TeamUpClient

mup_client = MeetupAdapterClient()
tup_client = TeamUpClient()


@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    return 'hello from Flask!'



@app.route('/groups')
def get_groups():
    return mup_client.get_group().text


@app.route('/calender')
def get_calendars():
    return tup_client.get_access().text


def get_sync():
    return tup_client.get_access().text


@app.cli.command()
def initdb():
    """Initialize the database."""
    db.create_all()

    example_mup = models.MeetupGroup(meetup_group_id='1')
    example_tup = models.TeamUpCalendar(team_group_id='1',
                                        meetup_group=example_mup)

    db.session.add(example_mup)
    db.session.add(example_tup)
    db.session.commit()
