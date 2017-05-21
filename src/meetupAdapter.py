import os

from src.baseAdapter import Client


class MeetupAdapterClient(Client):
    def __init__(self):
        api_key = os.environ.get("MEETUP_API_KEY")
        super().__init__(api_key)
        self.base_url = 'https://api.meetup.com'

    def get_group(self):
        url = self.construct_url(self.base_url, '/find/groups')
        request = self.make_request(url)
        return request


client = MeetupAdapterClient()

print(client.get_group().text)
