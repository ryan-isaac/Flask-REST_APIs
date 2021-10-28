import sqlite3

#start the connection
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#create the new user.
#auto increment is activated for the id column by typing the full word INTEGER
#instead of int along with PRIMARY KEY to use it as a unique key identifier
#the id will be assigned automatically
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)


connection.commit()

connection.close()
