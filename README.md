# Nursing Home Manager

Nursing home manager web application made with Django, using Oracle 19c database. Created for University course Databases and Big Data.

## Team
- Jan Lewandowski - https://github.com/iasiu
- Oskar Zając - https://github.com/zoskar

## Screenshots

<img src="pics/login.PNG" alt="Login page" width="640" height="360">
<img src="pics/caretaker_medicines.PNG" alt="Caretaker panel medicines view" width="640" height="360">
<img src="pics/manager_seniors.PNG" alt="Manager panel seniors view" width="640" height="360">
<img src="pics/doctor_seniors_healthcard_edit.PNG" alt="Doctor panel edit seniors healthcard view" width="640" height="360">

# Setup

## Global Requirements

1. Running locally oracle server 19c with newly created database
2. Installed instant_client
3. Installed python3
4. Installed pip
5. Installed git

## Windows
Clone repository and install dependencies
```shell
git clone https://github.com/iasiu/nursing-home-manager.git
cd nursing-home-manager
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```
Create new config file and give your Database name and password.
```shell
cd webapp
copy con config.py
NAME="databasename"
USER="system"
PASSWORD="userpassword"
```
Setup database from Django, create superuser and run server.
```shell
python manage.py makemigrations database
python manage.py migrate
python manage.py loaddata data.json
python manage.py createsuperuser
python manage.py runserver
```
## Linux/MacOS
Clone repository and install dependencies
```shell
git clone https://github.com/iasiu/nursing-home-manager.git
cd nursing-home-manager
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
Create new config file and give your Database name and password.
```shell
cd webapp
nano config.py
NAME="databasename"
USER="system"
PASSWORD="userpassword"
```
Setup database from Django, create superuser and run server.
```shell
python manage.py makemigrations database
python manage.py migrate
python manage.py loaddata data.json
python manage.py createsuperuser
python manage.py runserver
```
