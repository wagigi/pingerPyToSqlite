import sqlite3
import os
import time

conn = sqlite3.connect('base_ping.db')
hostname = "8.8.8.8"
response = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS ping(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     host TEXT ,
     up INTEGER ,
     date TEXT)""")
conn.commit()

# and then check the response...
if response == 0:
    print(hostname, 'is up!')
    cursor.execute(
        """INSERT INTO ping(host, up, date) VALUES(?, ?, ?)""", (hostname, 1, time.strftime("%d/%m/%Y %H:%M:%S")))
else:
    print(hostname, 'is down!')
    cursor.execute(
        """INSERT INTO ping(host, up, date) VALUES(?, ?, ?)""", (hostname, 0, time.strftime("%d/%m/%Y %H:%M:%S")))
conn.commit()
