import os
import sqlite3
from tkinter import *


dir_path = r"./databases"
res = []
flag = 0


for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

print(res)

name_input = input("Enter your name:")
name_input = name_input + ".db"
file = "./databases/" + name_input

for files in res:
    if files == name_input:
        flag = 1
        break

if flag == 1:
    print("Continue on GUI...")
    
    def add_db():
        equipment = clicked.get()
        conn = sqlite3.connect(file)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO equipment_issued VALUES (?)", (equipment,))
        conn.commit()
        conn.close()
    
    root = Tk()

    root.geometry( "500x500" )


    # Dropdown menu options
    options = [
        "Camera: ZWO 1600 MM pro monochrom ",
        "SOLARIX Solar filter (Explore Scientific -USA) - For RC 10",
        "Eyepieces: 40 mm",
        "Eyepieces: 25 mm",
        "Eyepieces: 15 mm",
        "Eyepieces: 9 mm",
        "Eyepieces: 4 mm"
    ]

    clicked = StringVar()
    clicked.set( "Camera: ZWO 1600 MM pro monochrom" )

    drop = OptionMenu( root , clicked , *options )
    drop.pack()

    # Create button, it will change label text
    button = Button( root , text = "Add to Cart" , command = add_db ).pack()
    
    root.mainloop()
else:
    print("Add your name to the database to continue...")