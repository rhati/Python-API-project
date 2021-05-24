import sqlite3
from flask_restful import Resource,reqparse

class User:
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password

    @classmethod
    def find_by_username(cls,username):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        select_query='select * from users where username=?'
        load=cursor.execute(select_query,(username,))

        row=load.fetchone()

        if row:
            user=cls(*row)

        else:
            user=None

        connection.close()

        return user

    @classmethod
    def find_by_id(cls,_id):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        select_query='select * from users where id=?'
        load=cursor.execute(select_query,(_id,))

        row=load.fetchone()

        if row:
            user=cls(*row)

        else:
            user=None

        connection.close()

        return user



class UserRegister(Resource):

    parse=reqparse.RequestParser()
    parse.add_argument('username',type=str,required=True,help='This field can not be blank')
    parse.add_argument('password',type=str,required=True,help='This field can not be blank')

    def post(self):

        data=UserRegister.parse.parse_args()

        if User.find_by_username(data['username']):
            return {'Message':"username is already exist, can't be register"}

        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        query='insert into users values(NULL,?,?)'
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.close()

        return {'message':'Credential has bee added successfully'},201