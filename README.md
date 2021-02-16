# Data Gouv

Projet Data Gouv Back :

-   Python 3.7
-   Django 3.1.6
-   Django Rest Framework 3.12.2
-   Postgresql 12

## First installation

Create virtual env :

> virtualenv --python python3.7 env (If you have python3.7 env variable), else
> virtualenv env

## Activate the virtual env (Windows):

> .\env\Scripts\activate

## Install requirements in env:

> pip install -r requirements.txt

## Create User and DB:

> psql -U postgres -f create_database_datagouv.sql

## Run DB migrations

> python manage.py makemigrations
> python manage.py migrate

## Restore the Dump

> psql datagouv < datagouv_bak.sql

## Run dev server

> python manage.py runserver

## Run unit tests

> coverage run .\manage.py test --verbosity=2

> coverage report -m

> coverage html

Then open htmlcov/index.html in your browser.
