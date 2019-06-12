# Django Authorization Project

## Initial Steps

1. Set the virtual environment `virtualenv -p python3 .` (To fix issue with `SyntaxError: Generator expression must be parenthesized` update Django to 1.11.17 `sudo pip3 install django==1.11.17`)
1. Activate it `source bin/activate`
1. Install Django 1.1 `sudo pip3 install django==1.11`
1. Save requirements `sudo pip3 freeze --local > requirements.txt`
1. Create a new project in root dir `django-admin startproject dj_auth .`
1. Add new app `django-admin startapp accounts`
1. Include new app in the `settings.py` file inside the `INSTALLED_APPS` array
1. Create a `.bash_aliases` file with the following `alias run='python3 manage.py runserver'`
1. To reload the `.bash_aliases` file we need to run `. ~/.bash_aliases`
1. We need to do django migration before we can run the server so `python3 manage.py migrate`