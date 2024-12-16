# GroceryFlow

## Running in production

See the ansible deploy.yml file for what's required to deploy an instance.

Other manual steps that are not included in the ansible file include:
- Setting up the nginx reverse proxy
- Installing pdflatex

To deploy the app, use:

```
ansible-playbook -i inventory.yml deploy.yml --vault-password-file keyfile
```

### Helpful Ansible Commands

```
# vault management
ansible-vault edit --vault-id @keyfile ./store.yml
ansible-vault create --vault-id @keyfile ./store.yml
ansible-vault view --vault-id @keyfile ./store.yml
ansible-vault rekey --vault-password-file ./keyfile --new-vault-password-file ./keyfile.new ./store.yml
```

### Nginx Reverse Proxy Setup

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

## Development

### Setting Up Development Environment

```
pre-commit install
source ./venv/bin/activate
python ./src/main.py
```

### Archiving Installed Dependencies

```
pip3 freeze > requirements.txt
```

## Task List

### User Feedback

For Sharing:
- agg ingredients by quantity
  - identify the quantity in the ingredient deck
  - sum the quantities for each ingredient
  - render quantity by each ingredient in latex
- I'd like to more easily be able to add recipes
- I'd like to more easily validate recipes that were added
  - use gpt for fitting recipes to schema
- I'd like to provide my own master list of item ordering so that the list order matches the order that I get stuff at the store
- I'd like to use this on my phone
- Instead of printing, I'd like to send the order to Doordash or Aldi for pickup

### Technical Nice To Have's
- Unit tests
- ditch legacy main.py

## Notes

Other:
- consider flask meld for dynamic ui https://www.flask-meld.dev/
