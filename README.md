# CRUD Flask-REST_APIs on sqlite3
This is a basic CRUD (Create, Read, Update, Delete) API testing for webservice application based on Flask. JWT is used to restrict access to specific users. For testing and development purposes, many variables have been hardcoded and the database used is SQLite as it is the most convenient in terms of size and functions for the purpose of this testing environment. The API requests were tested using "Postman" app on a Linux OS. 

## Files:
1- app.py <= This must be the main file to run (python3 app.py)
Starts Flask, sets the requests path, and imports all other files to run the web application

2- create_tables.py
Creates users and items tables in sqlite3 database

3- item.py
Defines the requests functions and how they interact with the database

4- security.py
Imports user.py to find users and matches them with existing users’ credentials to access the generated tokens

5- user.py
Defines functions to find or register users

Versions used in this virtual environment to run the program:
- Python==3.8.1
- Flask==2.0.2
- Flask-JWT==0.3.2
- Flask-RESTful==0.3.9
- PyJWT==1.4.2


## Run The Program
If interested in using the same versions, you may install and use a virtual environment in your directory for a clean python version of your selection. Below is how it can be installed on ubuntu Linux VM:
  
  #Install the virtual environment in the same directory of the code
  #Activate and access the virtual environment from the same directory, if it was successful, you will see (venv) before your path
          
    $> pip3 install virtualenv
    $> virtualenv venv --python=python3.8 
    $> source venv/bin/activate

Python will be running with a clean version with no modules installed. Inside the virtual environment, install these modules
  
    $> pip3 install Flask-Restful
    $> pip install Flask-JWT #json web token (we will encode the data)

  
Note: the venv folder where the virtual environment is installed, must be in the same folder where the database exists ("data.db") to allow it to be accessed by app.py.
