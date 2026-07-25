from src.storage import load_expenses, load_rates


def list_expenses(category: str | None = None, currency: str | None = None) -> None:
    expenses_list = load_expenses()
    if category:
        expenses_list = [
            expense for expense in expenses_list if expense["category"] == category
        ]
    if currency:
        rates_list = load_rates()
        rate = rates_list[currency]
        print(
            f"{'ID':<5} {'Date':<12} {'Description':<20} {'Category':<15} {'Amount (' + currency + ')':<15}"
        )

        for expense in expenses_list:
            expense["amount"] *= rate
    else:
        print(
            f"{'ID':<5} {'Date':<12} {'Description':<20} {'Category':<15} {'Amount (USD)':<15}"
        )

    for expense in expenses_list:
        print(
            f"{expense['id']:<5} {expense['date']:<12} {expense['description']:<20} {expense['category']:<15} {expense['amount']:<9.2f}"
        )
