import csv
from pathlib import Path
from src.storage import load_expenses


def export_expenses() -> None:
    expenses = load_expenses()
    fields = ["id", "date", "description", "amount", "category"]
    file_path = Path("exports/expenses.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(expenses)

    print(f"Successfully exported {len(expenses)} expenses to {file_path}")
