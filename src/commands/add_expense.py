from datetime import date
from src.schemas.expense import Expense
from src.storage import load_expenses, save_expenses


def add_expense(description: str, amount: float) -> None:
    expenses_list = load_expenses()

    if len(expenses_list) == 0:
        new_id = 1
    else:
        new_id = max(expense["id"] for expense in expenses_list) + 1

    expense_date = date.today().isoformat()
    expense: Expense = {
        "id": new_id,
        "date": expense_date,
        "description": description,
        "amount": amount,
    }
    expenses_list.append(expense)
    save_expenses(expenses_list)
    print(f"Expense added successfully (ID: {new_id})")
