from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    # add a foreign key for stores table
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # connect store_id to StoreModel to find a relationship (Foreign => Primary)
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    # create a class method to use it in different requests (GET, POST) without duplicating it
    # class method can be called by self or Item that is the class name
    @classmethod
    def find_by_name(cls,name):
        # SQLAlchemy converts this code to a query and returns an item model object
        return cls.query.filter_by(name=name).first() # converted to: "SELECT * FROM items WHERE name=name LIMIT 1"

        # sqlalchemy directly inserts an item to the database
    def save_to_db(self):
        # session is used to get a collection of objects that can be written at the database
        # the way SQLAlchemy works when adding, it adds an object if it doesn't exist or updates-
        # an existing object if it exists, for that, no update method is needed
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
