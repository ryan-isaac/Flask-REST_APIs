from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

# import custom made api
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)

# point at the database file that has been created at the root folder ///
# here you can set MySQL connection  by replacing the value with your mysql credentials "mysql://username:password@server/db"
#nevertheless, this will work on your local server
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# to know when an object changed but not saved, flask keeps track and it consumes resources
# to turn off this feature in flask but not in SQLAlchemy, the modifications tracker is set to False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# create a key for the encryption using Flask-JWT
app.secret_key = 'Jose'
# allows us to easily add resources
api = Api(app)

# python will run this function before running any request which will create a table as per app.config
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # it uses our codes and creates /auth endpoint

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, ('/item/<string:name>')) #http://127.0.0.1:5000/student/__name
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')

# to only run this file using python app.py, use "if __name__ == '__main__'"
# when a command is sent to run a file, python assigns the name '__main__' to the file
# this prevents running this file when importing it in other files
# otherwise, it will be running every time it gets imported into another file like item.py
# this file starts the flask app, therefore we don't need to start it unless we call python app.py
if __name__ == '__main__':
    db.init_app(app)
    app.run(port = 5000, debug=True)
