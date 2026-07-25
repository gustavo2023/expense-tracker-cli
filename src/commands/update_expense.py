from src.storage import load_expenses, save_expenses


def update_expense(
    id: int,
    description: str | None = None,
    amount: float | None = None,
    category: str | None = None,
) -> None:
    expenses_list = load_expenses()
    expense_found = False

    for expense in expenses_list:
        if expense["id"] == id:
            expense_found = True
            if description:
                expense["description"] = description
            if amount:
                expense["amount"] = amount
            if category:
                expense["category"] = category
            break

    if not expense_found:
        print(f"Expense not found (ID: {id})")
        return

    save_expenses(expenses_list)
    print(f"Expense updated successfully (ID: {id})")
