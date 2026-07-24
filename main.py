import argparse
from src.commands.add_expense import add_expense


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

    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument(
        "--id", required=True, type=int, help="ID of the expense to be edited"
    )
    update_parser.add_argument(
        "--date", type=str, help="Update the date of the expense"
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

    delete_parser = subparsers.add_parser("delete", help="Delete an existing expense")
    delete_parser.add_argument(
        "--id", required=True, type=int, help="ID of the expense to be deleted"
    )

    list_parser = subparsers.add_parser("list", help="View list of all expenses")

    summary_parser = subparsers.add_parser(
        "summary", help="View summary of all expenses"
    )
    summary_parser.add_argument(
        "--month",
        type=int,
        help="View summary of total expenses in a month",
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
        help="The new exchange rate (e.g., USD to VES)",
    )

    args = parser.parse_args()

    match args.command:
        case "add":
            add_expense(args.description, args.amount)
        case "update":
            print(f"Updating expense: {args.id}")
            if not args.date and not args.description and not args.amount:
                parser.error("You must provide at least one field to update.")
            else:
                if args.date:
                    print(f"Updating date: {args.date}")
                if args.description:
                    print(f"Updating description: {args.description}")
                if args.amount:
                    print(f"Updating amount: {args.amount}")
        case "delete":
            print(f"Deleting expense: {args.id}")
        case "list":
            print("Printing list of expenses")
        case "summary":
            if args.month:
                print(f"Printing summary of expenses for: {args.month}")
            else:
                print("Printing summary of expenses")
        case "set-rate":
            print(f"Setting new currency rate: {args.currency} - {args.rate}")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
