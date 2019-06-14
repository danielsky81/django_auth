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
1. Run `run`
1. Add github so `git init`, `git add .`, `git commit`, `git remote add origin https://github.com/danielsky81/django_auth.git` and finally `git push -u origin master`
1. Create a admin `python3 manage.py createsuperuser`

## Setting up templates

1. Adding `templates` folder to `accounts` app and `index.html` inside that folder
1. Add new view to the `views.py` file in order to serve the `index.html`
1. We now need to import the view inside the `urls.py` file like so `from accounts.views import index` and add the url `url(r'$', index),`

## Adding logout functionality

1. Adding `{% url 'logout' %}` inside the Logout anchor tag of my `index.html`
1. We need to create a new view. Prior to that we import auth so `from django.contrib import auth`. We need to add redirect and reverse to the new logout function `from django.shortcuts import render, redirect, reverse`
1. We need to add it to the `urls.py` file like this `url(r'^accounts/logout/$', logout, name="logout"),`. We give it a `name="logout"` so we can map it to the `index.html` where it is assigned to the anchor tag. We do the same for index, so `name="index"`. We need to import the logout from the views as well so `from accounts.views import logout`

## Django messages

1. In order to use this functionality we need to import it `from django.contrib import messages`
1. Then we add it to the logout function `messages.success(request, 'You have successfully been logged out!')`
1. Last step is to add it to the `settings.py` at the bottom like this `MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'`

## Adding login functionality and form

1. Same steps like with logout
1. Creating a `forms.py` file.
1. Importing forms to `views.py` as follows `from accounts.forms import UserLoginForm`
1. Django require to add the CSRF (Cross-Site Request Forgery) `{% csrf_token %}` inside the html

## Templates

1. Creating a `base.html` template in the root dir
1. To guide Django to that dir we need to add the following to the `TEMPLATES` inside the `settings.py` file `'DIRS': [os.path.join(BASE_DIR, 'templates')]`

## Authorization

The `login_required` decorator allows us to redirect users depending on whether or not they're authenticated. We just need to import it as follows `from django.contrib.auth.decorators import login_required` and add `@login_required` together to `views.py`

## Password reset via email

We can use console to print out the email required for reset (I think)

`EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`

or we can use real email via google:

```py
# settings.py
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = 587
```

## Email authentication

Django by default only supports logging in using a username. In order to facilitate an email login we need to build what is called a ***custom authentication back-end***. Authentication back-end is what django uses to authenticate users so we could create authentication backends to only log users in if they knew specific passcode.