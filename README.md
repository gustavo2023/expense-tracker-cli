# Expense Tracker CLI

## Overview

A robust Command Line Interface (CLI) application built in Python to manage personal finances. This tool allows users to track their daily expenses, view monthly summaries, set budgets, and export data. It also features a custom currency configuration system to seamlessly track expenses in multiple currencies (like USD and VES) without relying on external APIs.

## Requirements

The application runs entirely from the command line, utilizing `argparse` for command parsing and `uv` for package management and environment setup.

**Core Features:**

- Users can add an expense with a description and amount.
- Users can update an existing expense.
- Users can delete an expense.
- Users can view all expenses.
- Users can view a summary of all expenses.
- Users can view a summary of expenses for a specific month (of the current year).

**Advanced Features:**

- Add expense categories and allow users to filter expenses by category.
- Allow users to set a budget for each month and show a warning when the user exceeds the budget.
- Allow users to export expenses to a CSV file.
- Handle multiple currencies by allowing users to set a manual exchange rate via a local configuration state.

## Expected Commands & Output

```bash
# Adding expenses
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

# Viewing expenses
$ expense-tracker list
# ID  Date        Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

# Summaries
$ expense-tracker summary
# Total expenses: $30

$ expense-tracker summary --month 8
# Total expenses for August: $30

# Deleting expenses
$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20

# Setting custom exchange rate (e.g., USD to VES)
$ expense-tracker set-rate 40.50
# Exchange rate updated successfully.
```

## Project Roadmap

1. **The CLI Skeleton:** Set up the Python script using `argparse` to recognize subcommands (`add`, `list`, `delete`, etc.).
2. **Data Persistence:** Design the JSON data structure and create helper functions to read and write the data file securely.
3. **Core CRUD Operations:** Connect the CLI commands to the data functions to perform Create, Read, Update, and Delete actions on expenses.
4. **Logic and Summaries:** Implement filtering by date (e.g., monthly summaries) and calculating totals.
5. **The Advanced Features:** Introduce category filtering, the monthly budget warning system, and the CSV export functionality.
6. **The Currency Converter:** Implement the configuration file for the manual exchange rate and integrate currency conversion math into the summaries.
