
from pydantic import BaseModel


class Budget(BaseModel):
     category: str
     monthly_limit: float
     updated_date: str = ""