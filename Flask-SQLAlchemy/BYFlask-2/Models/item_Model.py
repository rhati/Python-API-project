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
            return cls(row[1],row[2])
        return None

    def Insert(self):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        insert='insert into items values(NULL,?,?)'
        cursor.execute(insert,(self.name,self.price,))
        connection.commit()
        connection.close()

    def delete(self):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        delete='delete from items where name=?'
        cursor.execute(delete,(self.name,))

        connection.commit()
        connection.close()

    def update(self):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        update='update items set price=? where name=?'
        cursor.execute(update,(self.price,self.name,))
        
        connection.commit()
        connection.close()