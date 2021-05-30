from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from Security import authenticate,Identity
from Resources.user import UserRegister,Credential
from Resources.item_same import Item,ItemsList
from Resources.store import Store,StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PROPAGATE EXCEPTIONS']=True
app.secret_key='Rahul'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,Identity)  #/auth

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/items/<string:name>')
api.add_resource(ItemsList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')
api.add_resource(Credential,'/Credential/<string:name>')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)