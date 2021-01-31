# .Blog
This project 

## Dependencies
Python 3
Django

## Usage
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
```.env
create a .env file in blogpost folder
add the following environment variables 
DEBUG = True/False
SECRET_KEY = your secret key
ALLOWED_HOST = your allowed hosts 
```

```db
in local.py uncomment the sql lite databse variable 
delete the other database variable
if you want you can set in the .env file the variables of your database
```

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```