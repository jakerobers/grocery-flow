# GroceryFlow

## Runbook

### Running in production

```
PYTHONPATH='src' gunicorn -w 4 -b 0.0.0.0:8000 src.main:app
```

### Archiving Installed Dependencies

```
pip3 freeze > requirements.txt
```

### Running development

```
pre-commit install
source ./venv/bin/activate
python ./src/main.py
```

## Tasks

Go to web:
- host on a server
- login page


## Notes

Other:
- consider flask meld for dynamic ui https://www.flask-meld.dev/
