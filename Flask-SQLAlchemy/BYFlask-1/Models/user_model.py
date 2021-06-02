import sqlite3
from flask_restful import Resource,reqparse


class UserModel:
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