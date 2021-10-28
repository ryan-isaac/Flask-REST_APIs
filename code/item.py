from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

#CRUPT Create Read Update Delete

#every resource has to be a class
class Item(Resource):
#--------------------------------------------------------#
# classmethods that can be accessed by all functions
#--------------------------------------------------------#
# this parser can be used for any method inside the class
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required = True,
        help="This field cannot be left blank!"
    )

    # create a class method to use it in different requests (GET, POST) without duplicating it
    # class method can be called by self or Item that is the class name
    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name= ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row != None:
            return {"item": {'name': row[0], 'price': row[1]}}

    # PUT can't update an existing item in sqlite3, therefore,
    # the creation of an item from POST method will be used as a classmethod
    # to be accessed in both PUT and POST requests
        # insert an item to the database
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # insert into the database
        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (item['name'],item['price']))

        connection.commit()
        connection.close()


    @classmethod
    def update(cls, item): #item parameter is a dictionaty of item and price
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # insert into the database
        query = "UPDATE items SET price=? WHERE name =?"
        cursor.execute(query, (item['price'],item['name']))

        connection.commit()
        connection.close()
#--------------------------------------------------------#
# class defined functions
#--------------------------------------------------------#

    jwt_required()
    def get(self,name):
        item = self.find_by_name(name)
        try:
            if item:
                return item
            return {'message': 'Item not found'}, 404
        except:
            return {'message': 'An error occured while fetching the data'}, 500

    @jwt_required()
    def post(self,name):
        # check that the item is not in the database
        if Item.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400 #bad request, client shoudl know item exists so they get bad request for trying to post a name that already exists
        # parse the data looking for price
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}

        try:
            self.insert(item)

        except:
            return{"message": "An error occured while inserting the item"}, 500 # 500 is for internal server error

        return item, 201

    @jwt_required()
    def delete(self, name):
        if Item.find_by_name != None:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            # delete row where name = item name from the table
            query = "DELETE FROM items WHERE name = ?"
            cursor.execute(query, (name,))
            connection.commit()
            connection.close()

            return {'message': 'Item deleted'}
        return {"message": "Item doesn't exist or an error occured while deleting"}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}

        if item == None:
            try:
                Item.insert(updated_item)
                return{"message":f"Item has been created {updated_item}"}
            except:
                return{"message": "An error occured while inserting the item."}, 500
        elif item != None:
            try:
                Item.update(updated_item)
                return{"message":f"New item has been updated {updated_item}"}
            except:
                return{"message": "An error occured while updating the item."}, 500
        else:
            return {"message": "Error Unknown"}
        return updated_item


class ItemList(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        # delete row where name = item name from the table
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = [] # create a list for all the items to be stored temporarily
        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()

        return {'items': items}
