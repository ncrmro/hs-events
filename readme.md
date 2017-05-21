# hs-events
Copy the dotenv file and add your API keys
`cp .env.sample .env`

Create and activate virtualenv
`python3 -m venv ~/.virtualenvs/hs-events/bin/activate`

`source ~/.virtualenvs/hs-events/bin/activate`

Install requirements
`pip3 install -r requirements.txt`

Start the flask server
`export FLASK_APP=hello.py flask run`

