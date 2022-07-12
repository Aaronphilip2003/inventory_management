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
        label.config(text=equipment)
        conn = sqlite3.connect(file)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO equipment_issued VALUES (?)", (equipment,))
        conn.commit()
        conn.close()

    root = Tk()

    root.geometry("450x450")
    root.title("SELECT THE ITEMS THAT YOU ARE ISSUING:")
    # Dropdown menu options
    options = [
        "Camera: ZWO 1600 MM pro monochrom ",
        "SOLARIX Solar filter (Explore Scientific -USA) - For RC 10",
        "ASI462MC(Color)",
        "Eyepieces: 40 mm",
        "Eyepieces: 25 mm",
        "Eyepieces: 15 mm",
        "Eyepieces: 9 mm",
        "Eyepieces: 4 mm",
        "GSO SuperView 20mm 1.15 Wide Angle Eyepiece",
        "GSO 2 inch 99% Quartz Dielectric mirror Diagonal CNC",
        "GSO 2x ED-Barlow-Lens (Multicoated)",
        "T-RING Canon M42",
        'T Adapter 1.25" ',
        "Eyepiece Projection Camera Adapter",
        "Mobile Cell Phone Adapter",
        "GSO 1.25",
        "32mm Camera Projection Lens (CPL) eyepiece",
        "COMA Corrector 2 inch",
        'GSO 0.5X Focal Reducer 1.25" with 25mm extension tube',
        "GSO ND Filter 25% GSO ND Filter 50%",
        "60mm GUIDE SCOPE",
        "Green Laser Pointer with rechargeable battery",
        'NexGen 2" Laser Collimator for Telescopes',
        "Astro R-Lite Red Flashlight for Astronomy",
        "Eyepiece and Accessory Soft Case",
        "Dessicant Cap 1.25 inch",
        "ZWO NB7nmD31",
        "ZWO EFW 8*1.25”",
        "ZWO LRGBI.25NEW",
        "ZWO EAF-with HC",
        "ZWO ASI AIR PLUS",
        "ZWO 12V 5A AC to DC Adapter for cooled cam & AIRPro",
        "ZWO UV IR Cut filter-1.25”",
    ]

    clicked = StringVar()
    clicked.set("Camera: ZWO 1600 MM pro monochrom")

    drop = OptionMenu(root, clicked, *options)
    drop.pack()

    # Create button, it will change label text
    button = Button(root, text="Add to Cart", command=add_db).pack()

    label = Label(root, text=" ")
    label.pack()

    root.mainloop()
else:
    print("Add your name to the database to continue...")
