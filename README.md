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

Deploying:

```
ansible-playbook -i inventory.yml deploy.yml --vault-password-file keyfile
```

Ansible-related activity

```
# vault management
ansible-vault edit --vault-id @keyfile ./store.yml
ansible-vault create --vault-id @keyfile ./store.yml
ansible-vault view --vault-id @keyfile ./store.yml
ansible-vault rekey --vault-password-file ./keyfile --new-vault-password-file ./keyfile.new ./store.yml
```

Nginx Reverse Proxy

```
# /etc/nginx/sites-available/groceryflow
server {
    listen 80;
    server_name groceryflow.jakerobers.com;

    location / {
        proxy_pass http://unix:/var/www/groceryflow/groceryflow.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Then enable it:

```
sudo ln -s /etc/nginx/sites-available/groceryflow /etc/nginx/sites-enabled
sudo systemctl restart nginx
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
- host on a server (left off on deploying this. get ansible command to succeed and then do nginx stuff)

## Notes

Other:
- consider flask meld for dynamic ui https://www.flask-meld.dev/
