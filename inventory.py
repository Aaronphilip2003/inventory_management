from tkinter import *
import sqlite3
import os

conn=sqlite3.connect("people.db")
cursor=conn.cursor()

cursor.execute("SELECT * FROM names")
table=cursor.fetchall()

list_names=[]

for row in table:
    list_names.append(row[0])
print(list_names)

conn.close()

for i in list_names:
    conn=sqlite3.connect(os.path.join('./databases',f"{i}.db"))
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS equipment_issued(equipment_name)")
    conn.close()