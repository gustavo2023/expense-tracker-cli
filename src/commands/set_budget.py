import calendar
from src.storage import load_budgets, save_budgets


def set_budget(month: int, amount: float) -> None:
    budgets = load_budgets()
    budgets[str(month)] = amount
    save_budgets(budgets)
    print(f"Budget of {amount:.2f} set successfully for {calendar.month_name[month]}")
