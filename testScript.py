import sqlite3

conn = sqlite3.connect("data/processed/vgc.db")
cur = conn.cursor()

cur.execute("SELECT DISTINCT category FROM battle_stats")
for row in cur.fetchall():
    print(row)

conn.close()