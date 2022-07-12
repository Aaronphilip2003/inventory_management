import os
import sqlite3

dir_path = r"./databases"

res = []
flag = 0
eq = "TELESCOPE"

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
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO equipment_issued VALUES (?)", (eq,))
    conn.commit()
    conn.close()

