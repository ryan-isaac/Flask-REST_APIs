import sqlite3
from flask_restful import Resource, reqparse

# user object instead of dictionaries
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    # since we will use the class name User in "if row: user = User(row[0]...)"
    # we should make it a class method to use the current class instead of hardcoding the class name if it will be changed in the future
    @classmethod
#ability to retrieve user object from the database by interacting with sqlite3
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # search the table for a given username
        query = "SELECT * FROM users WHERE username=?" # select only the rows where the username matches the parameter
        # get the result of the query
        result = cursor.execute(query, (username,)) # username must be in a tuple so we leave a comma
        # get the first row from the result set if more than one
        row = result.fetchone()
        # if it wasn't None, if there is a found result
        if row:
            #create a user object with the data from that row for(row[0], row[1], row[2]) the 3 columns is, username, password
            # instead of specifying the number of rows, we can use positional arguments (*args)
            # change (row[0], row[1], row[2]) to (*row)
            user = cls(*row)
        else:
            # return None if not found
            user = None

        connection.close()

        #return the user or None id not found
        return user

    # since we will use the class name User in "if row: user = User(row[0]...)"
    # we should make it a class method to use the current class instead of hardcoding the class name if it will be changed in the future
    @classmethod
#ability to retrieve user object from the database by interacting with sqlite3
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # search the table for a given username
        query = "SELECT * FROM users WHERE id=?" # select only the rows where the username matches the parameter
        # get the result of the query
        result = cursor.execute(query, (id,)) # username must be in a tuple so we leave a comma
        # get the first row from the result set if more than one
        row = result.fetchone()
        # if it wasn't None, if there is a found result
        if row:
            #create a user object with the data from that row for(row[0], row[1], row[2]) the 3 columns is, username, password
            # instead of specifying the number of rows, we can use positional arguments (*args)
            # change (row[0], row[1], row[2]) to (*row)
            id = cls(*row)
        else:
            # return None if not found
            id = None

        connection.close()

        #return the user or None id not found
        return id

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
        # "if User.find_by_username" returns True if user exists, None if it doesn't
        if User.find_by_username(data['username']):
            return{"messager": "A user with that username already exists"}, 400
        #connect to the database and create a cursor
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # insert the values into the table with null as the id
        query = "INSERT INTO users VALUES (NULL, ?, ?)" # null for the id as it auto increment
        cursor.execute(query, (data['username'], data['password']))# username, pass has to be a tuple

        #save the changes
        connection.commit()
        connection.close()

        # response 201 for created
        return {"message": "User created successfully."}, 201
