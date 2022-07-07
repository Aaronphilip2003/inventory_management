from tkinter import *
import sqlite3

conn=sqlite3.connect("people.db")
cursor=conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS names(first_name text)")

def insert():
    name=e.get()
    cursor.execute("INSERT INTO names VALUES (?)",(name,))
    conn.commit()
    e.delete(0,END)


root=Tk()
root.geometry("500x300")

lbl_main=Label(root,text="Database Entry")
lbl_main.place(x=180,y=50)

e_label1=Label(root,text="First Name : ")
e_label1.place(x=50,y=100)

e=Entry(root, borderwidth=5, width=50)
e.place(x=120,y=100)


button_insert=Button(root,text="INSERT",command=insert)
button_insert.place(x=200,y=200)
root.mainloop()

conn.close()