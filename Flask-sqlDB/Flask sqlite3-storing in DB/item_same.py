import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required


class Item(Resource):

    parse=reqparse.RequestParser()
    parse.add_argument('price',type=float,required=True,help='This field can not be blank')

    @classmethod
    def find_by_item_name(cls,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        query='select * from items where name=?'
        load=cursor.execute(query,(name,))
        row=load.fetchone()

        connection.close()

        if row:
            return {'name':row[1],'price':row[2]}
        return None

    def get(self,name):
        if self.find_by_item_name(name):
            return self.find_by_item_name(name)
        return {'message':'The Item is not exist'}
        
    def post(self,name):

        if self.find_by_item_name(name):
            return {"Message":"The item is exist with the name {}".format(name)},400

        #response=request.get_json()
        response=Item.parse.parse_args()

        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        insert='insert into items values(NULL,?,?)'
        cursor.execute(insert,(name,response['price'],))
        connection.commit()
        connection.close()
        
        return self.find_by_item_name(name)

    @jwt_required()
    def delete(self,name):
        item=self.find_by_item_name(name)
        if item:
            connection=sqlite3.connect('data.db')
            cursor=connection.cursor()

            delete='delete from items where name=?'
            cursor.execute(delete,(name,))
            connection.commit()
            connection.close()
            return {"Message":"The Items has been deleted"}
        return {"message":"The item has not been found"},404


    def put(self,name):
        #response=request.get_json()
        response=Item.parse.parse_args()
        item=self.find_by_item_name(name)

        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        if item:
            update='update items set price=? where name=?'
            cursor.execute(update,(response['price'],name,))
            connection.commit()
            connection.close()
            return {'message':'Item has been updated'}

        insert='insert into items values(NULL,?,?)'
        cursor.execute(insert,(name,response['price'],))
        connection.commit()
        connection.close()
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
