from flask_restful import Resource,reqparse
from Models.user_model import UserModel
from flask_jwt import jwt_required

class UserRegister(Resource):

    parse=reqparse.RequestParser()
    parse.add_argument('username',type=str,required=True,help='This field can not be blank')
    parse.add_argument('password',type=str,required=True,help='This field can not be blank')

    def post(self):

        data=UserRegister.parse.parse_args()
        cred=UserModel.find_by_username(data['username'])

        if cred:
            return {'Message':"username is already exist, can't be register"},400

        cred=UserModel(**data)
        cred.save_to_db()

        return {'message':'Credential has been added successfully'},201


class Credential(Resource):

    parse=reqparse.RequestParser()
    parse.add_argument('password',type=str,required=True,help='This field can not be blank')

    
    @jwt_required()
    def get(self,name):
        credential=UserModel.find_by_username(name)
        if credential:
            return {"username":name,'password':credential.password}

        return {"message":"The user not found"}

    @jwt_required()
    def delete(self,name):
        credential=UserModel.find_by_username(name)
        if credential:
            credential.delete_to_db()
            return {"message":"The credential has been deleted"}
        return {"message":"The credential is not found"}

    @jwt_required()
    def put(self,name):
        credential=UserModel.find_by_username(name)
        passwd=Credential.parse.parse_args()
        if credential is None:
            credential=UserModel(name,**passwd)
            credential.save_to_db()
            return {"Message":"The password has been added"}
        
        credential.password=passwd['password']
        credential.save_to_db()
        return {"Message":"The password has been updated"}
        
        


