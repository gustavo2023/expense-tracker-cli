import json
from pathlib import Path
from schemas.expense import Expense

EXPENSES_FILE = Path("src/data/expenses.json")
RATES_FILE = Path("src/data/rates.json")


def _ensure_directory(file_path: Path) -> None:
    directory = file_path.parent

    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)


def load_expenses() -> list[Expense]:
    _ensure_directory(EXPENSES_FILE)

    if not EXPENSES_FILE.is_file():
        return []

    with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def save_expenses(expenses_list: list[Expense]) -> None:
    _ensure_directory(EXPENSES_FILE)

    with open(EXPENSES_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses_list, file, indent=4)


def load_rates() -> dict[str, float]:
    _ensure_directory(RATES_FILE)

    if not RATES_FILE.is_file():
        return {}

    with open(RATES_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def save_rates(rates_list: dict[str, float]) -> None:
    _ensure_directory(RATES_FILE)

    with open(RATES_FILE, "w", encoding="utf-8") as file:
        json.dump(rates_list, file, indent=4)
