# App Name
Email Alert App

## Description
This is a web app that allows users to sign up and recieve email alerts through text messages in thei mobile phones

## User Stories
* A user can sign in to the application
* A user can create a profile and set profile with your preffered email
* A user can delete their accout 
* A user can choose the phone number they would love to recieve alerts on
* A an authorized user can rate the app 
* A user can add or change the phone number to get alerts from
* A user can add or change the email that he/she recieves alerts from
*  

## Set Up and Installation

#### Prerequisites

* Python 3.6.2
* Virtual environment
* Postgres Database
* Reliable Internet Connection

## Installation Process

* Copy repolink

in your terminal run the following commands

* $ git clone REPO-URL in your terminal
* $ cd watch
* $ python3.6 -m venv virtual
* $ touch .env ( to the file add :
        SECRET_KEY=<your secret key>
        DEBUG=True)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt
* $ psql ; CREATE DATABASE instagram ;

In the settings.py module of the project make the following changes

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'alert',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}

* $ python3.6 manage.py runserver (this command runs the application of port http://127.0.0.1/8000 )
 
## Known Bugs

No known bugs

## CREDITS

Moringa School,Python Documentation, StackOverflow.com and W3 schools

## Technologies Used

This project uses major technologies which are :

* HTML5/CSS
* Bootstrap
* Python3.6
* Django Frane Work
* Postgress Database

## Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through khalifngeno@gmail.com or leave a comment here on github.

## License 

Copyright MIT [LiCENSE](./LICENSE) (c) 2017 [Kipngetich Ngeno](https://github.com/Kipngetich33)

