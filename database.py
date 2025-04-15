import sqlite3 as sql

conn = sql.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE finalProject (name TEXT, checkIn TEXT, checkOut TEXT, roomType TEXT)')
print("Table created successfully")
conn.close()