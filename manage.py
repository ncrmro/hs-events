from src import app, MeetupAdapterClient, TeamUpClient

mup_client = MeetupAdapterClient()
tup_client = TeamUpClient()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/groups')
def get_groups():
    return mup_client.get_group().text


@app.route('/calender')
def get_calendars():
    return tup_client.get_access().text
