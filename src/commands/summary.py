import calendar
from datetime import date
from src.storage import load_expenses, load_rates


def summary(month: int | None = None, currency: str | None = None) -> None:
    expenses_list = load_expenses()

    if month:
        target_prefix = f"{date.today().year}-{month:02d}"
        expenses_list = [
            expense
            for expense in expenses_list
            if expense["date"].startswith(target_prefix)
        ]

    total = sum(expense["amount"] for expense in expenses_list)
    currency_label = "USD"

    if currency:
        rates_list = load_rates()
        rate = rates_list[currency]
        total *= rate
        currency_label = currency

    if month:
        month_name = calendar.month_name[month]
        print(f"Total expenses for {month_name} ({currency_label}): ${total:.2f}")
    else:
        print(f"Total expenses ({currency_label}): ${total:.2f}")
