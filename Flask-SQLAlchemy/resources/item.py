from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

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
        help="Every item needs a price"
    )

    parser.add_argument('store_id',
        type=int,
        required = True,
        help="Every item needs a store id"
    )
#--------------------------------------------------------#
# class defined functions
#--------------------------------------------------------#

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        try:
            if item: #not None
                return item.json()
            else:
                return {'message': 'Item not found'}, 404
        except:
            return {'message': 'An error occured while fetching the data'}, 500

    @jwt_required()
    def post(self,name):
        # check that the item is not in the database
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400 #bad request, client shoudl know item exists so they get bad request for trying to post a name that already exists
        else:
            data = Item.parser.parse_args()
            item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return{"message": "An error occured while inserting the item."}, 500 # 500 is for internal server error

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        try:
            if item:
                item.delete_from_db()
            else:
                return {'message': 'Item: [ {} ] does not exist'.format(name)}

            return {'message': 'Item: [ {} ] has been deleted'.format(name)}

        except:
            return {"message": "Item doesn't exist or an error occured while deleting"}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        try:
            if item is None:
                item = ItemModel(name, **data)
            else:
                item.price = data['price']

            item.save_to_db()

            return{"message":f"Item has been saved {item.json()}"}

        except:
            return{"message": f"An error occured while inserting the item {item.json()}."}, 500



class ItemList(Resource):
    @jwt_required()
    def get(self):
        # return a list of all items using query

        return {'items': [item.json() for item in ItemModel.query.all()]}
