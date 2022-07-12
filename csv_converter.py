import sqlite3
import pandas as pd
import os 
res=[]
dir_path= r"./databases"
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

for i in res:
    header = []
    conn = sqlite3.connect(f"{dir_path}/{i}")
    c = conn.cursor()
    for column in c.execute('PRAGMA table_info("equipment_issued")'):
        header.append(column[1])
        df = pd.DataFrame(columns=header)
    for raw in c.execute("SELECT * FROM equipment_issued ORDER BY equipment_name"):
        s = pd.Series(list(raw), index=df.columns)
        df = df.append(s, ignore_index=True)
    df.to_csv(f"{i[:-3]}.csv")

    
# header = []
#conn = sqlite3.connect(path)
# c = conn.cursor()
# for column in c.execute('PRAGMA table_info("equipment_issued")'):
#     header.append(column[1])

# df = pd.DataFrame(columns=header)
# for raw in c.execute("SELECT * FROM equipment_issued ORDER BY equipment_name"):
#     s = pd.Series(list(raw), index=df.columns)
#     df = df.append(s, ignore_index=True)
# df.to_csv("NEERAJ.csv")
