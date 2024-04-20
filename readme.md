## Activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install requirements

```bash
pip3 install -r requirements/prod.txt
```

## Install requirements for development

```bash
pip3 install -r requirements/dev.txt

```

## Setup env variables

In **'config.env'** you have a list of env variables required for project.\
Copy them into **'.env'**, replace values if necessary

## Run project

```bash
pip3 install -r requirements/prod.txt\
python3 manage.py runserver
```

