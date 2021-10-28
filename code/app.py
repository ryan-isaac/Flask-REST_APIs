from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# import custom made api
from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
# create a key for the encryption using Flask-JWT
app.secret_key = 'Jose'
#allows us to easily add resources
api = Api(app)


jwt = JWT(app, authenticate, identity) # it uses our codes and creates /auth endpoint




api.add_resource(Item, ('/item/<string:name>')) #http://127.0.0.1:5000/student/__name
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


# to only run this file using python app.py, use "if __name__ == '__main__'"
# when a command is sent to run a file, python assigns the name '__main__' to the file
# this prevents running this file when importing it in other files
# otherwise, it will be running every time it gets imported into another file like item.py
# this file starts the flask app, therefore we don't need to start it unless we call python app.py
if __name__ == '__main__':
    app.run(port = 5000, debug=True)
