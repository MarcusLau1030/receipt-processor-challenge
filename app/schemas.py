from pydantic import BaseModel

class Item(BaseModel):
    shortDescription: str
    price: str

    
class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[Item]
    total: str    

