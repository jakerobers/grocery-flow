Run dev webserver: python ./src/main.py
Source env: source ./venv/bin/activate
Snapshotting deps: pip3 freeze > requirements.txt

Go to web:
- socket notifies client that the document is ready with /document url (https://flask-sock.readthedocs.io/en/latest/quickstart.html#example)
- /document/{{uuid}} opens in a new tab
- document prints from web


Notes:
- consider flask meld for dynamic ui https://www.flask-meld.dev/
