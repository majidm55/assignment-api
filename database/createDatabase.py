import sqlite3
conn = sqlite3.connect("content_management.db")
columns = [
    "id INTEGER PRIMARY KEY",
    "title VARCHAR",
    "url TEXT",
    "thumbnail TEXT",
]
create_table_cmd = f"CREATE TABLE contents ({','.join(columns)})"
conn.execute(create_table_cmd)
