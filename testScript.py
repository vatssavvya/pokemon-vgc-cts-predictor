import sqlite3

conn = sqlite3.connect("data/processed/vgc.db")
cur = conn.cursor()

cur.execute("""
    SELECT rank, hp_points, attack_points, defense_points,
           sp_atk_points, sp_def_points, speed_points, percentage
    FROM battle_stats
    WHERE pokemon = 'Garchomp' AND category = 'stat_points'
    ORDER BY rank
""")
for row in cur.fetchall():
    print(row)

conn.close()