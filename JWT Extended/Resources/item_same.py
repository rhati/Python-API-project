from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required,get_jwt_identity,verify_jwt_in_request
from Models.item_Model import ItemModel


class Item(Resource):

    parse=reqparse.RequestParser()
    parse.add_argument('price',type=float,required=True,help='This field can not be blank')
    parse.add_argument('store_id',type=int,required=True,help='Every Item need the store id')

    def get(self,name):

        if ItemModel.find_by_item_name(name):
            return (ItemModel.find_by_item_name(name)).json()

        return {'message':'The Item is not exist'}
        
    def post(self,name):

        if ItemModel.find_by_item_name(name):
            return {"Message":"The item is exist with the name {}".format(name)},400

        #response=request.get_json()
        response=Item.parse.parse_args()

        item=ItemModel(name,**response)

        item.save_to_db()
        
        return item.json(),201

    @jwt_required()
    def delete(self,name):
        claims=get_jwt_identity()
        
        if claims['is_admin']==False:
            return {"Message":"Admin Privilage Required"},401


        item=ItemModel.find_by_item_name(name)
        if item:
            item.delete()
            return {"Message":"The Items has been deleted"}
        return {"message":"The item has not been found"},404


    def put(self,name):
        #response=request.get_json()
        response=Item.parse.parse_args()
        item=ItemModel.find_by_item_name(name)

        if item is None:
            item=ItemModel(name,**response)
        else:
            item.price=response['price']

        item.save_to_db()
        return item.json()


class ItemsList(Resource):
    def get(self):
        return {"items":[item.json() for item in ItemModel.find_all()]}
        #return {"items":list(map(lambda x:x.json(),ItemModel.query.all()))}
