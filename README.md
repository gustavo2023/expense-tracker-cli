# Expense Tracker CLI

## Overview

A robust Command Line Interface (CLI) application built in Python to manage personal finances. This tool allows users to track their daily expenses, view monthly summaries, set budgets, and export data. It also features a custom currency configuration system to seamlessly track expenses in multiple currencies (like USD and VES) without relying on external APIs.

## Features

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
# Adding an expense category
$ expense-tracker category "Food"

# Adding expenses
$ expense-tracker add --description "Lunch" --amount 20 --category "Food"
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10 --category "Food"
# Expense added successfully (ID: 2)

# Viewing expenses
$ expense-tracker list
# ID  Date        Description  Category  Amount
# 1   2024-08-06  Lunch        Food      $20.00
# 2   2024-08-06  Dinner       Food      $10.00

# Summaries
$ expense-tracker summary
# Total expenses: $30.00

$ expense-tracker summary --month 8
# Total expenses for August: $30.00

# Deleting expenses
$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20.00

# Setting custom exchange rate (e.g., USD to VES)
$ expense-tracker set-rate --currency VES --rate 40.50
# Exchange rate updated successfully.
```

## Installation Guide

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd expense-tracker
   ```

2. **Set up the environment:**
   This project uses `uv` for package management. Ensure `uv` is installed, then sync the environment:

   ```bash
   uv sync
   ```

3. **Run the application:**
   To make the `expense-tracker` command available globally in any terminal directory while actively developing, install it in editable mode using `uv tool`:

   ```bash
   uv tool install -e .
   ```

   Now you can use the CLI directly from anywhere:

   ```bash
   expense-tracker --help
   ```
