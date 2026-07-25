import csv
from pathlib import Path
from src.storage import load_expenses, load_rates


def export_expenses(currency: str | None = None) -> None:
    expenses = load_expenses()
    fields = ["id", "date", "description", "amount", "category"]
    file_path = Path("exports/expenses.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if currency:
        file_path = Path(f"exports/expenses_{currency}.csv")
        rates_list = load_rates()
        rate = rates_list[currency]

        for expense in expenses:
            expense["amount"] *= rate

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(expenses)

    print(f"Successfully exported {len(expenses)} expenses to {file_path}")
