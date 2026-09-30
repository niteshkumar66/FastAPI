from fastapi import FastAPI

from schemas import Ship,UpdateShipment
from db import Database


app = FastAPI()
db = Database("supply.db")

@app.get("/shipments/{sid}")
def get_shipments(sid):
    pass


@app.post("/create-shipment/")
def create_shipment(data:Ship):
    new_id = db.new_shipment(data)
    return {"new_id":new_id}

@app.put("/update-shipment/{sid}")
def update_shipment(sid: int, data: UpdateShipment):
    