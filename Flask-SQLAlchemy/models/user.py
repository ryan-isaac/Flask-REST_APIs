from db import db

class UserModel(db.Model):
    __tablename__ = 'users' # table name for SQLAlchemy to use
    # set the columns for SQLAlchemy for this model
    # only these properties/columns will be used in this model
    # using id as a variable isn't ideal since it is a builtin python method but it is ok-
    # in our case to avoid confusing names in the database
    id = db.Column(db.Integer, primary_key=True) # primary key means auto increment. it is auto-filled by SQLAlchemy
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, username, password):
        # the columns can be defined here but they will not be used by the model since they-
        # are not defined above and they will not give an error as well
        # id column is automatically created, no need to hardcode it here since it's a primary key
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        # query builder allows us to run a query directly in SQLAlchemy
        # sqlalchemy will run select * where username=username limit 1 and return an object
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        # sqlalchemy will run select * where id=id limit 1 and return an object
        return cls.query.filter_by(id=id).first()
