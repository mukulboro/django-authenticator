# TOTP Authentication workflow in Django
 This project implements a TOTP authentication workflow using Authenticator apps in Django. 
 ## Features
 - Simple and well documented.
 - No external authentication library used.
 - Utilized Django auth, forms and messages.
 - Only used internal Django libraies and the `qrcode` package to implement the workflow.

 ## Installation
 - Clone and `cd` into the repository.
 - `pip install -r requirements.txt` to install all required packages.
 - `python manage.py migrate` to create the database and all databse tables.
 - `python manage.py createsuperuser` to create an admin account
 - `python manage.py runserver` to run the server on port 8000.

 ## Usage
 - `/admin` to access the Django admin panel.
 - `/register` to create a user account.
 - `/login` to login using new account.
 - `/` to access dashboard.\
*You will view other relevant routes as you use the application*

