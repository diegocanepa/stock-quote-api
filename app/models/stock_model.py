from pydantic import BaseModel
from typing import List

class StockQuote(BaseModel):
    symbol: str
    price: float
    date: str

class StockListResponse(BaseModel):
    available_stocks: List[str]
