import sqlite3
from flask_restful import Resource,reqparse
from Models.user_model import UserModel

class UserRegister(Resource):

    parse=reqparse.RequestParser()
    parse.add_argument('username',type=str,required=True,help='This field can not be blank')
    parse.add_argument('password',type=str,required=True,help='This field can not be blank')

    def post(self):

        data=UserRegister.parse.parse_args()
        cred=UserModel.find_by_username(data['username'])

        if cred:
            return {'Message':"username is already exist, can't be register"},400

        cred=UserModel(data['username'],data['password'])
        cred.save_to_db()

        return {'message':'Credential has been added successfully'},201
