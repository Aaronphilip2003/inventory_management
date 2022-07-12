import sqlite3
import pandas as pd

path = "./databases/AARON.db"
conn = sqlite3.connect(path)

header = []
c = conn.cursor()
for column in c.execute('PRAGMA table_info("equipment_issued")'):
    header.append(column[1])

df = pd.DataFrame(columns=header)
for raw in c.execute("SELECT * FROM equipment_issued ORDER BY equipment_name"):
    s = pd.Series(list(raw), index=df.columns)
    df = df.append(s, ignore_index=True)
df.to_csv("AARON.csv")
