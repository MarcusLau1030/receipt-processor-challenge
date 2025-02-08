from typing import Union

from fastapi import FastAPI, HTTPException
from app.schemas import Item, Receipt
from app.rules import Rules
from app.responses import Responses

app = FastAPI()

# hashmap with receipts as keys and ids as values
id_receipt = dict()

# hashmap with id as keys and points as values
id_points = dict()

# It seems as the goal of this api is to return points for each receipt, so if duplicate receipts are inputed we can skip the calculations and reuse the points

@app.get("/")
def read_root():
    return {"Hello": "Fetch team :)"}

@app.post("/receipts/process")
async def process_receipt(receipt: Receipt):
    try:
        if receipt not in id_receipt.values():
            unique_id = id(receipt)
            id_receipt[unique_id] = receipt
        return unique_id
    except Exception as e:
        response_400 = Responses.NotFound
        raise HTTPException(status_code=response_400["status_code"], detail=response_400["description"])
        

@app.get("/receipts/{id}/points")
def read_receipts_id_points(id: int):
    if id in id_points:
        return id_points[id]
    
    if id not in id_receipt:
        response_404 = Responses.BadRequest()
        raise HTTPException(status_code=response_404["status_code"], detail=response_404["description"])

    receipt = id_receipt[id]
    total_points = 0
    
    rules_list = [func_name for func_name in dir(Rules) if callable(getattr(Rules, func_name)) and func_name.startswith("r_")]
    
    for func_name in rules_list:
        method = getattr(Rules, func_name, None)
        total_points += method(receipt)

    return {"points": total_points}