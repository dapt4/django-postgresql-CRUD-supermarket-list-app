# django-postgresql-CRUD-supermarket-list-app

![image](https://user-images.githubusercontent.com/67972962/185005757-756cee1e-7f1a-4f69-a77a-ea46e0f0931a.png)


first create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requeriments

`$ pip install -r requirements.txt`

install postgresql, login and create the database

`CREATE DATABASE <yourDBname>;`

create a .env file in the root folder

`$ touch .env`

and add your postgresql credentials and the app SECRET_KEY to .env file

>ENV_SECRET_KEY="{add a secret key like bhajfbkjhawbdkjhabdjh}"\
ENV_NAME='{yourDBname}'\
ENV_HOST='{your host or localhost}'\
ENV_PORT='{your db port or 5432}'\
ENV_USER='{your db user}'\
ENV_PASSWORD='{your db password}'
run the command:

`python manage.py migrate`

finally the project run with: 

`$ python manage.py runserver`

open your browser in: 

`localhost:8000/`



