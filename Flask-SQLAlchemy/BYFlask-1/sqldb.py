import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_table="create table IF NOT EXISTS users (id INTEGER PRIMARY KEY,username text,password text)"
cursor.execute(create_table)

insert_query="insert into users values (?,?,?)"
users=[(1,'RHPM','1234'),(2,'ash','as2s'),(3,'mh','daa5')]
cursor.executemany(insert_query,users)


create_itemtable='create table IF NOT EXISTS items (id INTEGER PRIMARY KEY,name text,price text)'
cursor.execute(create_itemtable)
    
connection.commit()

connection.close()