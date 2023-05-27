import sys
from os.path import dirname, abspath

# Add the 'app' directory to the system path
app_path = dirname(dirname(abspath(__file__)))
sys.path.append(app_path)

import sqlite3
conn = sqlite3.connect("content_management.db")
import app.globals.data as globalsData

def createTable():
    for data in globalsData.CONTENT:
        id = data["id"]
        title = data["title"]
        url = data["url"]
        thumbnail = data["thumbnail"]
        insert_cmd = f"INSERT INTO contents VALUES ('{id}', '{title}', '{url}', '{thumbnail}')"
        conn.execute(insert_cmd)

    conn.commit()

createTable()
