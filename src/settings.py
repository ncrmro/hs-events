import os
from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask

BASE_DIR = dirname(dirname(__file__))

# Load dotenv file
dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)
env = os.environ

DB_URL = env.get("DB_URL")
TEAMUP_API_KEY = env.get("TEAMUP_API_KEY")
MEETUP_API_KEY = env.get("MEETUP_API_KEY")

app = Flask(__name__)
