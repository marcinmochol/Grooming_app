Before start working with application prepare virtual environment:

    Download application's files:
        git clone <repository_name>;

    Open PyCharm or another IDE;

    Install:
        django 3.10.0 or newer,
        psycopg2-binary (newest: 2.9.3),
        pytest,
        pytest-django;

    Create database and configure local_setting.py file:

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

    Make migrations:
        python manage.py makemigrations
        python manage.py migrate
    Run server:
        python manage.py runserver

