import sqlite3

class Database:
    def __init__(self,db_name):
        self.con=sqlite3.connect(db_name)
        self.cur=self.con.cursor()
        self.create_table("shipments")
        
    def create_table(self,name:str):
        self.cur.execute(f"""
            CREATE TABLE IF NOT EXIST {name}
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            weight REAL,
            status TEXT
            )
""")

        self.con.commit()

db = Database("supply.db")


def new_shipment(self,shipments:Ship):
    self.cur.execute(
        """
    
"""
    )