import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from Models.item_Model import ItemModel


class Item(Resource):

    parse=reqparse.RequestParser()
    parse.add_argument('price',type=float,required=True,help='This field can not be blank')

    def get(self,name):

        if ItemModel.find_by_item_name(name):
            return (ItemModel.find_by_item_name(name)).json()

        return {'message':'The Item is not exist'}
        
    def post(self,name):

        if ItemModel.find_by_item_name(name):
            return {"Message":"The item is exist with the name {}".format(name)},400

        #response=request.get_json()
        response=Item.parse.parse_args()

        item=ItemModel(name,response['price'])

        item.Insert()
        
        return item.json(),201

    @jwt_required()
    def delete(self,name):
        item=ItemModel.find_by_item_name(name)
        if item:
            item.delete()
            return {"Message":"The Items has been deleted"}
        return {"message":"The item has not been found"},404


    def put(self,name):
        #response=request.get_json()
        response=Item.parse.parse_args()
        item=ItemModel(name,response['price'])

        if ItemModel.find_by_item_name(name):
            item.update()
            return {'message':'Item has been updated'}

        item.Insert()
        return {'message':'Item has been added'}


class ItemsList(Resource):
    def get(self):
        items=[]
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        select_items="select * from items"
        for i in cursor.execute(select_items):
            items.append({"name":i[1],'price':i[2]})

        return {'items':items}
