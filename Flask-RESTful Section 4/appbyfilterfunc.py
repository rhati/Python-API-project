from flask import Flask,request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

Items=[
        {
        "name": "Iphone",  
        "price": "599"
        }
    ]

class Item(Resource):
    def get(self,name):
        item=next(filter(lambda x:x['name']==name,Items),None)
        return {'item':item},200 if item else 404


    def post(self,name):

        if next(filter(lambda x:x['name']==name,Items),None):
            return {"Message":"The item is exist with the name {}".format(name)},400

        response=request.get_json()
        item={'name':name,'price':response['price']}
        Items.append(item)
        return item,201


    def delete(self,name):
        item=next(filter(lambda x:x['name']==name,Items),None)
        if item:
            Items.remove(item)
            return {"Message":"The Items has been deleted"}
        return {"message":"The item has not been found"},404


    def put(self,name):
        response=request.get_json()
        item=next(filter(lambda x:x['name']==name,Items),None)
        if item:
            Items[Items.index(item)]={'name':name,'price':response['price']}
            return {'message':'Item has been updated'}

        item={'name':name,'price':response['price']}
        Items.append(item)
        return {'message':'Item has been added'}


class ItemsList(Resource):
    def get(self):
        return {"Items":Items}


api.add_resource(Item,'/items/<string:name>')
api.add_resource(ItemsList,'/items')
app.run(port=5000,debug=True)