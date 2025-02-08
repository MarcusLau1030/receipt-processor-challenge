
class Responses:
    
    def BadRequest():
        return {"status_code": 400, "description": "The receipt is invalid."}
    
    def NotFound():
        return {"status_code": 404, "description": "No receipt found for that ID."}