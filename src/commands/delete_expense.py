from src.storage import load_expenses, save_expenses


def delete_expense(expense_id: int) -> None:
    expenses_list = load_expenses()
    new_expenses_list = [
        expense for expense in expenses_list if expense["id"] != expense_id
    ]

    if len(new_expenses_list) == len(expenses_list):
        print("Error: Expense ID not found")
    else:
        save_expenses(new_expenses_list)
        print("Expense deleted successfully")
