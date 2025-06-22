from pydantic import BaseModel
from datetime import datetime

class OrderOut(BaseModel):
    id: int
    created_at: datetime
    total_price: float
