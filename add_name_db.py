import sqlite3
import os

from matplotlib.pyplot import table

conn=sqlite3.connect('people.db')
cursor=conn.cursor()

cursor.execute("SELECT * FROM names")
table=cursor.fetchall()

list_names=[]

for row in table:
    list_names.append(row[0])

for i in list_names:
    with open(os.path.join('./databases',f"{i}.db"), "a") as file:
        file.write("test")