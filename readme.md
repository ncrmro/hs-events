# hs-events
Copy the dotenv file and add your API keys
`cp .env.sample .env`

Create and activate virtualenv, zappa complains if venv and project are the same name.
`python3 -m venv ~/.virtualenvs/hs-events-venv`

`source ~/.virtualenvs/hs-events-venv/bin/activate`

Install requirements
`pip3 install -r requirements.txt`

Create and stage databse
`export FLASK_APP=manage.py && flask initdb`

Start the flask server
`export FLASK_APP=manage.py && flask run`


## Deployment
Lamda

`pip install awscli`

`aws configure`

...

```

AWS Access Key ID: foo
AWS Secret Access Key: bar
...
```

`zappa deploy dev`

`zappa schedule dev`

`zappa tail dev`

Don't forget to unschedule dev!!!
`zappa unschedule production`

`zappa update dev`

`zappa undeploy dev`

`zappa deploy production`

Schedule CloudWatch to run src.sync every 5 minutes.
`zappa schedule prod`