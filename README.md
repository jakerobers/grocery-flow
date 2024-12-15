# GroceryFlow

## Runbook

Run dev webserver: python ./src/main.py
Source env: source ./venv/bin/activate
Snapshotting deps: pip3 freeze > requirements.txt
Running in prod: PYTHONPATH='src' gunicorn -w 4 -b 0.0.0.0:8000 src.main:app


## Tasks

Go to web:
- host on a server
- login page


## Notes

Other:
- consider flask meld for dynamic ui https://www.flask-meld.dev/
