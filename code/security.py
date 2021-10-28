from user import User
# import user class from user.py

#use sqlite3 database and this allows the program to retrieve users from the database

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
