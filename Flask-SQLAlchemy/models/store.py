from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # reference ItemModel for a relationship with this table. many to on in this case
    # avoid creating object (store connection) for each item by setting lazy to dynamic
    # this can be avoided but creating the store might get slower, while using lazy will make fetching data slower
    items = db.relationship('ItemModel', lazy= 'dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]} #.all() is used when lazy parameter is used in relationship as it changes from list of items to a query builder that looks for the item name

    # Will be used to find a store by name and add or update a store
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
        connection.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
