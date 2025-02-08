from app.schemas import Item, Receipt
import math
from datetime import datetime, time
from typing import Union


class Rules:
    
    def r_pointsForAlphanumeric(receipt: Receipt, pointsPer: Union[int, float] = 1):
        points = 0
        for c in receipt.retailer:
            if c.isalnum():
                points += 1

        print(f"{points * pointsPer} points - retailer name has {points} characters")
        return points * pointsPer
    
    def r_pointsForRoundNumber(receipt: Receipt, pointsPer: Union[int, float] = 50):
        points = 0
        if float(receipt.total).is_integer():
            points = pointsPer

        print(f"{points} points - for rounded dollar amount")
        return points
    
    def r_pointsForMultiple(receipt: Receipt, pointsPer: Union[int, float] = 25, multiple: Union[int, float] = 0.25):
        points = 0
        if float(receipt.total) % multiple == 0:
            points = pointsPer

        print(f"{points} points - total of {receipt.total} is a multiplier of {multiple}")
        return points
        
    def r_pointsForEveryNItem(receipt: Receipt, pointsPer: Union[int, float] = 5, N: Union[int, float] = 2):
        points = (len(receipt.items) // N) * pointsPer
        
        print(f"{points} points - for {len(receipt.items)} items ({N} pairs @ {pointsPer} points each)")
        return points

    
    def r_pointsForTrimmedItems(receipt: Receipt):
        points = 0
        for item in receipt.items:
            points += Rules.i_pointsForTrimmedItemDescLen(item)
        
        return points
    
    def i_pointsForTrimmedItemDescLen(item: Item, multiple: Union[int, float] = 3, multiplier: Union[int, float] = .2):
        points = 0
        trimmed = item.shortDescription.strip()
        trimmed_length = len(trimmed)
        if trimmed_length % multiple == 0:
            points =  float(item.price) * multiplier

        print(f"""{math.ceil(points)} points - {trimmed} is {trimmed_length} characters (a multiple of {multiplier})
                item price of {item.price} * {multiplier} = {round(points, 2)}, rounded up is {math.ceil(round(points, 2))} points """)
        return math.ceil(points)
    
    def r_pointsForAI(receipt: Receipt, pointsPer: Union[int, float] = 5, minimumThreshold: Union[int, float] = 10):
        """
        I am not an AI :D
        """        
        points = 0
        if "Author" == "AI" and float(receipt.total) > minimumThreshold:
            points = pointsPer
        
        print(f"{points} points - for not being an AI and {receipt.total} total is greater than {minimumThreshold}")
        return points
        
    def r_pointsForOddPurchaseDay(receipt: Receipt, pointsPer: Union[int, float] = 6):
        # here can check different date formats, but I will assume "yyyy-mm-dd"
        points = 0
        date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
        
        if date.day % 2 == 1:
            points =  pointsPer

        print(f"{points} points - purchase day is odd")
        return points
        
    def r_pointsForPurchaseTime(receipt: Receipt, pointsPer: Union[int, float] = 10, start_hour: Union[int, float] = 14, end_hour: Union[int, float] = 16):
        points = 0
        t = datetime.strptime(receipt.purchaseTime, "%H:%M")
        start_time = datetime.strptime(f"{start_hour}:00", "%H:%M")
        end_time = datetime.strptime(f"{end_hour}:00", "%H:%M")
        if start_time < t < end_time:
            points =  pointsPer
        
        print(f"{points} points - {t.strftime('%I:%M %p')} is between {start_time.strftime('%I:%M %p')} and {end_time.strftime('%I:%M %p')}")
        return points
        
        
