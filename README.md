# contactbook-services
contact book services for different clients

How to Setup Project:

### Dependencies ###
* Python 3.x
* PostGreSQL 9.x

### Getting Started ###
create a database for application 
create database contact_book_services 

### take a clone of repository

1. Creat a fork of my respository on Github 
2. git clone https://github.com/Meenu2415/contactbook-services.git
3. Creat a python environment - virtualenv -p python3 envcontactbook
4. Activate the environment - source envcontactbook/bin/activate
5. Update the setting files with your database
6. Install the required packages for this project in activated env run the command 
	pip install -r requirements.txt
7. Run migrations: "python manage.py migrate"
8. Create superuser: "python manage.py createsuperuser"



### Running Sample API from DRF ###

1. Go to http://127.0.0.1:8000/admin/ and login with your superuser credentails
2. once you logged in add some relationship 
3. Go to http://127.0.0.1:8000/o/applications/
4. Register a new application with Client Type (Confidential) and Authorization Grant Type (Resource Owner Password Based)
5. Change OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET in appconfig.py with the ones created in the new application

Finally You are ready to use the Rest APIs - 

python manage.py runserver

Go through the API Doc and start using APIs

#How to run testcase 

pytest

############# If any issue for setup contact to +918123961170 ################


