# GroceryFlow

## Runbook

### Environment file

```
# .env

# generated with `openssl rand -hex 32`
SESSION_KEY=72ec47560a9ab6303af9fb3b7938212b4be8d31bbdb15da2465a277c55ff0dee
PYTHONPATH='src'
FILE_GEN_OUTPUT_DIR=/tmp/files
```

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
