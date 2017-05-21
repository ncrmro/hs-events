from os.path import join, dirname

import requests
from dotenv import load_dotenv

BASE_DIR = dirname(dirname(__file__))

dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


class Client:
    def __init__(self, api_key):
        self.api_key = api_key

    def initialize(self):
        return self.api_key

    def make_request(self, url):
        payload = {'key': self.api_key}
        request = requests.get(url, params=payload)
        return request

    def construct_url(self, base_url, endpoint):
        data = {'base_url': base_url, 'endpoint': endpoint}
        url = '{base_url}{endpoint}'.format(**data)
        return url
