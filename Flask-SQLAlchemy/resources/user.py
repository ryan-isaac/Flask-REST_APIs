import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type= str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('password',
        type= str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        # get the data from json payload
        # parse the argument that expects a username and a password
        data = UserRegister.parser.parse_args()

        #make sure not to register a duplicate username
        # find_by_username returns the username or None if the user doesn't exist
        # "if UserModel.find_by_username" returns True if user exists, None if it doesn't
        if UserModel.find_by_username(data['username']):
            return{"messager": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        # response 201 for created
        return {"message": "User created successfully."}, 201
