## Installation

Before start working with application prepare virtual environment:

```bash
  pip install virtualenv
```

Download application's files:  
```bash
  git clone <repository_name>
``` 
Install:

    django 3.10.0 or newer,
    psycopg2-binary (newest: 2.9.3),
    pytest,
    pytest-django

Create database and configure local_setting.py file:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database_name>',
        'HOST': 'localhost',
        'PASSWORD': '<password>',
        'USER': '<username>',
        'PORT': 5432
    }
}
```   
Make migrations:  
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```  
Run server: 
```bash
python manage.py runserver
```
