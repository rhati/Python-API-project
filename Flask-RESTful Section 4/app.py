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
        for i in range(len(Items)):
            if Items[i]['name']==name:
                return Items[i]
        return {"message":"The item has not been found"},404


    def post(self,name):
        response=request.get_json()
        item={'name':name,'price':response['price']}
        Items.append(item)
        return item,201


    def delete(self,name):
        for i in range(len(Items)):
            if Items[i]['name']==name:
                Items.remove(Items[i])
                return {"Message":"The Items has been deleted"}
        return {"message":"The item has not been found"},404


    def put(self,name):
        response=request.get_json()
        for i in range(len(Items)):
            
            if Items[i]['name']==name:
                Items[i]={'name':name,'price':response['price']}
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