# CRUD Flask-REST_APIs on sqlite3
This is a basic CRUD (Create, Read, Update, Delete) API testing for webservice application based on Flask.  JWT is used to restrict access to specific users. For testing and development purposes, many variables has been hardcoded and the database used is sqlite as it's the most convenient in terms of size and functions for the purpose of this testing environment. The API requests were tested using "Postman" app on a linux OS. 

## Files:


The main app.py file imports the codes from other files to run the program. 

Versions used in this virtual environment to run the program:
- Python==3.8.1
- Flask==2.0.2
- Flask-JWT==0.3.2
- Flask-RESTful==0.3.9
- PyJWT==1.4.2


If interested in using the same versions, you may install and use a virtual environment in your directory for a clean python version of your selection. Below is how I installed it on my ubuntu linux VM:
  
  #Install the virtual environment in the same directory of the code
  #Activate and access the virtual environment from the same directory, if it was succssful, you will see (venv) before your path
          
    $> pip3 install virtualenv
    $> virtualenv venv --python=python3.8 
    $> source venv/bin/activate

Python will be running with a clean version with no modules installed. Inside the virtual environment, install these modules
  
    $> pip3 install Flask-Restful
    $> pip install Flask-JWT #json web token (we will encode the data)

  
Note: the venv folder where the virtual environment is installed must be in the same folder where the database exists ("data.db") in order to have it accessed by app.py file.


