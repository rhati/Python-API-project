from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from Security import authenticate,Identity
from user import UserRegister
from item_same import Item,ItemsList



app=Flask(__name__)
app.secret_key='Rahul'
api=Api(app)

jwt=JWT(app,authenticate,Identity)  #/auth


api.add_resource(Item,'/items/<string:name>')
api.add_resource(ItemsList,'/items')
api.add_resource(UserRegister,'/register')

if __name__=='__main__':
    app.run(port=5000,debug=True)