from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from Resources.user import UserRegister,Credential,UserLogin
from Resources.item_same import Item,ItemsList
from Resources.store import Store,StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PROPAGATE EXCEPTIONS']=True
app.secret_key='Rahul' #we can use app.config['JWT_SECRET_KEY']
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWTManager(app)

@jwt.user_identity_loader
def add_claims_to_jwt(identity):
    if identity==1:
        return {'is_admin':True}
    return {'is_admin':False}

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/items/<string:name>')
api.add_resource(ItemsList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')
api.add_resource(Credential,'/Credential/<string:name>')
api.add_resource(UserLogin,'/login')


if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)