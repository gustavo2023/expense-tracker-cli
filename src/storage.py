import json
from pathlib import Path
from typing import Any
from src.schemas.expense import Expense

EXPENSES_FILE = Path("src/data/expenses.json")
RATES_FILE = Path("src/data/rates.json")
CATEGORIES_FILE = Path("src/data/categories.json")


def _ensure_directory(file_path: Path) -> None:
    directory = file_path.parent

    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)


def _load_json(file_path: Path, default_value: Any) -> Any:
    _ensure_directory(file_path)
    if not file_path.is_file():
        return default_value
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def _save_json(file_path: Path, data: Any) -> None:
    _ensure_directory(file_path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_expenses() -> list[Expense]:
    return _load_json(EXPENSES_FILE, [])


def save_expenses(expenses_list: list[Expense]) -> None:
    _save_json(EXPENSES_FILE, expenses_list)


def load_rates() -> dict[str, float]:
    return _load_json(RATES_FILE, {})


def save_rates(rates_list: dict[str, float]) -> None:
    _save_json(RATES_FILE, rates_list)


def load_categories() -> list[str]:
    return _load_json(CATEGORIES_FILE, [])


def save_categories(categories_list: list[str]) -> None:
    _save_json(CATEGORIES_FILE, categories_list)
