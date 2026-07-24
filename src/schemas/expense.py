from typing import TypedDict

class Expense(TypedDict):
    id: int
    date: str
    description: str
    amount: float