import sys
import argparse
import calendar
from src.commands.add_expense import add_expense
from src.commands.delete_expense import delete_expense
from src.commands.add_category import add_category
from src.commands.list_expenses import list_expenses
from src.commands.set_rate import set_rate
from src.commands.summary import summary
from src.commands.update_expense import update_expense
from src.commands.set_budget import set_budget
from src.commands.export import export_expenses
from src.storage import load_categories, load_rates, load_budgets


def main():
    parser = argparse.ArgumentParser(
        prog="Expense Tracker CLI", description="CLI app to manages expenses"
    )
    subparsers = parser.add_subparsers(
        dest="command", help="Available commands for the Expense Tracker application"
    )

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument(
        "--description", required=True, type=str, help="Description of the expense"
    )
    add_parser.add_argument(
        "--amount", required=True, type=float, help="Amount of the expense"
    )
    add_parser.add_argument(
        "--category", required=True, type=str, help="Category of the expense"
    )

    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument(
        "--id", required=True, type=int, help="ID of the expense to be edited"
    )

    update_parser.add_argument(
        "--description",
        type=str,
        help="Update the description of an expense",
    )
    update_parser.add_argument(
        "--amount",
        type=float,
        help="Update the amount of an expense",
    )
    update_parser.add_argument(
        "--category", type=str, help="Update the category of an expense"
    )

    delete_parser = subparsers.add_parser("delete", help="Delete an existing expense")
    delete_parser.add_argument(
        "--id", required=True, type=int, help="ID of the expense to be deleted"
    )

    list_parser = subparsers.add_parser("list", help="View list of all expenses")
    list_parser.add_argument(
        "--category", type=str, help="Filter expenses by a category"
    )
    list_parser.add_argument(
        "--currency", type=str, help="List expenses in using a different currency"
    )

    summary_parser = subparsers.add_parser(
        "summary", help="View summary of all expenses"
    )
    summary_parser.add_argument(
        "--month",
        type=int,
        help="View summary of total expenses in a month",
    )
    summary_parser.add_argument(
        "--category", type=str, help="View summary of total expenses in a category"
    )
    summary_parser.add_argument(
        "--currency", type=str, help="View summary using a different currency"
    )

    set_rate_parser = subparsers.add_parser(
        "set-rate", help="Set the exchange currency rate"
    )
    set_rate_parser.add_argument(
        "--currency", required=True, type=str, help="Currency of the new rate"
    )
    set_rate_parser.add_argument(
        "--rate",
        required=True,
        type=float,
        help="The new exchange rate (e.g., USD to EUR)",
    )
    category_parser = subparsers.add_parser("category", help="Add an expense category")
    category_parser.add_argument("category", type=str, help="Expense category to add")

    budget_parser = subparsers.add_parser("budget", help="Create a budget for a month")
    budget_parser.add_argument(
        "--month", required=True, type=int, help="Month of the budget"
    )
    budget_parser.add_argument(
        "--amount", required=True, type=float, help="Amount of the budget"
    )

    export_parser = subparsers.add_parser(
        "export", help="Export expenses to a CSV file"
    )

    args = parser.parse_args()

    match args.command:
        case "add":
            if not args.description.strip():
                parser.error("The description cannot be empty")
            if args.amount <= 0:
                parser.error("The expense amount must be greater than zero")

            valid_categories = load_categories()
            if args.category not in valid_categories:
                response = input(
                    f"Category '{args.category}' does not exist. Do you want to add it? (y/n): "
                )
                if response.lower() in ["y", "yes"]:
                    add_category(args.category)
                else:
                    parser.error(
                        f"Invalid category. Must be one of: {', '.join(valid_categories)}"
                    )
            add_expense(args.description, args.amount, args.category)
        case "update":
            if not args.description and not args.amount and not args.category:
                parser.error("You must provide at least one field to update.")
            if args.description is not None and not args.description.strip():
                parser.error("The description cannot be empty")
            if args.amount is not None and args.amount <= 0:
                parser.error("The expense amount must be greater than zero")
            if args.category:
                valid_categories = load_categories()
                if args.category not in valid_categories:
                    parser.error(
                        f"Invalid category. Must be one of: {', '.join(valid_categories)}"
                    )
            update_expense(args.id, args.description, args.amount, args.category)
        case "delete":
            if args.id <= 0:
                parser.error("You must provide a valid positive ID")
            delete_expense(args.id)
        case "list":
            if args.category:
                valid_categories = load_categories()
                if args.category not in valid_categories:
                    parser.error(
                        f"Invalid category. Must be one of: {', '.join(valid_categories)}"
                    )
            if args.currency:
                rates = load_rates()
                if args.currency not in rates:
                    parser.error(
                        f"Currency '{args.currency}' not found. Add it firts using the 'set-rate' command."
                    )
            list_expenses(args.category, args.currency)
        case "summary":
            summary(args.month, args.currency)
        case "set-rate":
            rates = load_rates()

            if args.currency in rates:
                current_rate = rates[args.currency]
                response = input(
                    f"Currency '{args.currency}' already exists (Rate: '{current_rate}'). Update to '{args.rate}'? (y/n): "
                )

                if response.lower() not in ["y", "yes"]:
                    print("Action cancelled")
                    sys.exit(0)
            set_rate(args.currency, args.rate)
        case "category":
            if not args.category.strip():
                parser.error("The category cannot be empty")
            add_category(args.category)
        case "budget":
            if not 1 <= args.month <= 12:
                parser.error("The month must be a valid integer between 1 and 12")
            if args.amount < 0:
                parser.error("The budget amount cannont be negative")

            budgets = load_budgets()
            if str(args.month) in budgets:
                current_budget = budgets[str(args.month)]
                month_name = calendar.month_name[args.month]
                response = input(
                    f"Budget for {month_name} already exists (Amount: '{current_budget:.2f}'). Update to '{args.amount:.2f}'? (y/n): "
                )

                if response.lower() not in ["y", "yes"]:
                    print("Action cancelled")
                    sys.exit(0)
            set_budget(args.month, args.amount)
        case "export":
            export_expenses()
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
