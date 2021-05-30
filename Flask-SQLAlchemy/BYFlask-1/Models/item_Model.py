import sqlite3

class ItemModel:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def json(self):
        return {'name':self.name,'price':self.price}

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

    @classmethod
    def Insert(cls,item):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        insert='insert into items values(NULL,?,?)'
        cursor.execute(insert,(item['name'],item['price'],))
        connection.commit()
        connection.close()

    @classmethod
    def delete(cls,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        delete='delete from items where name=?'
        cursor.execute(delete,(name,))

        connection.commit()
        connection.close()

    @classmethod
    def update(cls,item):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        update='update items set price=? where name=?'
        cursor.execute(update,(item['price'],item['name'],))
        
        connection.commit()
        connection.close()