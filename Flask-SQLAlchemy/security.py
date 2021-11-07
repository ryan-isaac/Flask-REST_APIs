from models.user import UserModel
# import user class from user.py

#Allows the program to retrieve users from the database

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    #if user is not None and the password = the password in the database
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
