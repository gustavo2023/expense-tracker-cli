import calendar
from datetime import date
from src.schemas.expense import Expense
from src.storage import load_expenses, save_expenses, load_budgets


def add_expense(description: str, amount: float, category: str) -> None:
    expenses_list = load_expenses()

    if len(expenses_list) == 0:
        new_id = 1
    else:
        new_id = max(expense["id"] for expense in expenses_list) + 1

    today = date.today()
    expense_date = today.isoformat()
    current_month = today.month
    budgets = load_budgets()

    if str(current_month) in budgets:
        budget_limit = budgets[str(current_month)]
        current_total = sum(
            expense["amount"]
            for expense in expenses_list
            if int(expense["date"][5:7]) == current_month
        )

        if current_total + amount > budget_limit:
            print(
                f"⚠️  WARNING: This expense exceeds your budget of ${budget_limit:.2f} for {calendar.month_name[current_month]}!"
            )
            print(
                f"   Current spent: ${current_total:.2f} | New total will be: ${(current_total + amount):.2f}"
            )
            
    expense: Expense = {
        "id": new_id,
        "date": expense_date,
        "description": description,
        "amount": amount,
        "category": category,
    }
    expenses_list.append(expense)
    save_expenses(expenses_list)
    print(f"Expense added successfully (ID: {new_id})")
