# CRUD Flask-REST APIs With SQLite3 and MySQL Databases
This is a basic CRUD (Create, Read, Update, Delete) API testing for webservice application based on Flask. JWT is used to restrict access to specific users. For testing and development purposes, many variables have been hardcoded for SQLite database as it is the most convenient in terms of size and functions for the purpose of this testing environment. The API requests were tested using "Postman" app on a Linux OS. Another version with more flexible varibales is created using SQLAlchemy which allows for better querying and less hardcoding. 

## Flask-SQLite Files:
  1- app.py <= This must be the main file to run (python3 app.py) \
Starts Flask, sets the requests path, and imports all other files to run the web application

  2- create_tables.py \
Creates users and items tables in sqlite3 database

  3- item.py \
Defines the requests functions and how they interact with the database

  4- security.py \
Imports user.py to find users and matches them with existing users’ credentials to access the generated tokens

  5- user.py \
Defines functions to find or register users

## Flask-SQLAlchemy Files:
  1- app.py
  The main file to run the program, import the models and resources, set the SQLAlchemy configurations (refer to: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/), initiate the table creation, and set the api paths.
  2- db.py
  Set Flask SQLAlchemy() object db, to use it in other files.
  3- security.py
  Allows the program to retrieve users from the database
  4- models
    - item
    Defines item table columns and includes all models needed to run the resource file related to items table and its connection with other tables (finding an item, deleting an item, or posting an item).
    - store
    Defines store table columns and includes all models needed to run the item resource file and defines its connection with item ItemModel that connects both tables.
    - user
    Defines users table columns and includes all models needed to register a user or find a user.
    
  5-Resources
    - item
    - store
    - user
    Define the allowed api request types and authorization type "JWT". Use the models' files for accessing the tables, perform the requested actions, and define the json messages to be sent back to the end user

Versions used in this virtual environment to run the program:
- Python==3.8.1
- Flask==2.0.2
- Flask-JWT==0.3.2
- Flask-RESTful==0.3.9
- PyJWT==1.4.2

## Run The Program
If interested in using the same versions to avoid any version issues, you may install and use a virtual environment in your directory for a clean python version without affecting your current installed version. Below is how it can be installed on ubuntu Linux VM:
  
  #Install the virtual environment in the same directory of the code
  #Activate and access the virtual environment from the same directory, if it was successful, you will see (venv) before your path
          
    $> pip3 install virtualenv
    $> virtualenv venv --python=python3.8 
    $> source venv/bin/activate

Python will be running with a clean version with no modules installed. Inside the virtual environment, install these modules
  
    $> pip install Flask
    $> pip install Flask-Restful # this installs Flask automatically, but you can also install it separately 
    $> pip install Flask-JWT #json web token (we will encode the data)
    $> pip install Flask-SQLAlchemy 

  
Note: the venv folder where the virtual environment is installed, must be in the same folder where the database exists ("data.db") to allow it to be accessed by app.py.
