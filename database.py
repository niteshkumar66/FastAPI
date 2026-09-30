import sqlite3

Connection = sqlite3.connect("sql.db")

cur = Connection.cursor()
cur.execute(
''' 
CREATE TABLE IF NOT EXISTS shipments (
id INTEGER, 
weight REAL , 
content TEXT,
status TEXT)
'''
)

# cur.execute(
# """
# INSERT INTO shipments VALUES(
# 1273,
# 1.0,
# "charger",
# "packed"
# )
# """
# )


cur.execute(
"""
SELECT  * FROM shipments WHERE id = ?
""" (id)
)


data = (cur.fetchone())

print(data)

Connection.commit()
Connection.close()