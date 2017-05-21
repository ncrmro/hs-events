from os.path import join, dirname

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = dirname(dirname(__file__))

dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
