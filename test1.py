import sqlite3

db = sqlite3.connect('Database.db')
cursor = db.cursor()
sql  = "select * from car;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()

print("Hello World")
print("Hello World")