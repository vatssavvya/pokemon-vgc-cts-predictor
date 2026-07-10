import json
import os
import sqlite3

RAW_DIR = os.path.join("data", "raw")
DB_PATH = os.path.join("data", "processed", "vgc.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS battle_stats (
    pokemon TEXT NOT NULL,
    format TEXT NOT NULL,
    season TEXT NOT NULL,
    category TEXT NOT NULL,
    rank INTEGER,
    name TEXT NOT NULL,
    percentage REAL,
    stat_up TEXT,
    stat_down TEXT,
    hp_points INTEGER,
    attack_points INTEGER,
    defense_points INTEGER,
    sp_atk_points INTEGER,
    sp_def_points INTEGER,
    speed_points INTEGER
);

CREATE INDEX IF NOT EXISTS idx_pokemon_category
    ON battle_stats (pokemon, category);
"""


def ensure_dirs():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)


def load_battle_file(conn, filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    pokemon = data["pokemon"]
    fmt = data["format"]
    season = data["season"]

    rows = data.get("rows", [])
    if not rows:
        print(f"WARNING: no rows found in {filepath} — check the file manually.")
        return 0

    def clean(value):
        # The API uses "" for empty numeric fields instead of null.
        # Convert those to None so SQLite stores real NULLs.
        return None if value == "" else value

    cur = conn.cursor()
    for row in rows:
        cur.execute(
            """
            INSERT INTO battle_stats (
                pokemon, format, season, category, rank, name, percentage,
                stat_up, stat_down, hp_points, attack_points, defense_points,
                sp_atk_points, sp_def_points, speed_points
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                pokemon,
                fmt,
                season,
                row.get("category"),
                row.get("rank"),
                row.get("name"),
                row.get("percentage_value"),  # pre-parsed float, not the "89.1%" string
                clean(row.get("stat_up")),
                clean(row.get("stat_down")),
                clean(row.get("hp_points")),
                clean(row.get("attack_points")),
                clean(row.get("defense_points")),
                clean(row.get("sp_atk_points")),
                clean(row.get("sp_def_points")),
                clean(row.get("speed_points")),
            ),
        )
    conn.commit()
    return len(rows)


def main():
    ensure_dirs()
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)

    total = 0
    for filename in os.listdir(RAW_DIR):
        if filename.startswith("battle_") and filename.endswith(".json"):
            filepath = os.path.join(RAW_DIR, filename)
            count = load_battle_file(conn, filepath)
            print(f"{filename}: inserted {count} rows")
            total += count

    conn.close()
    print(f"\nDone. {total} total rows written to {DB_PATH}")


if __name__ == "__main__":
    main()