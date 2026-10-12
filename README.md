# Expense Tracker

A simple, menu-driven **Expense Tracker** built with Python. This beginner-friendly command-line application helps users record expenses, view their spending, calculate total expenses, and see a category-wise summary.

## Features

- **Add Expense:** Enter a category, amount, and description.
- **View Expenses:** Display all recorded expenses.
- **Total Expenses:** Calculate the sum of recorded amounts.
- **Category Summary:** View total spending grouped by category.
- **Exit:** Close the application from the menu.

## Technologies Used

- Python 3
- Python lists, dictionaries, loops, functions, and user input

## Project Structure

```text
Expense-Tracker/
├── ExpenseTracker.py
├── README.md
└── requirements.txt
```

## Getting Started

1. Install [Python 3](https://www.python.org/downloads/).
2. Clone the repository or download the files.
3. Open a terminal in the project directory.
4. Run:

```bash
python ExpenseTracker.py
```

On some systems, use `python3 ExpenseTracker.py` instead.

## How to Use

The program displays the following menu:

```text
===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. View Total Expenses
4. Category Summary
5. Exit
```

Select an option by entering its number. For example, choose `1` and enter:

```text
Enter category: Food
Enter amount: 150
Enter description: Lunch
Expense added successfully.
```

Choose `4` to view a category-wise summary, or `3` to see the total of all recorded expenses.

## Requirements

- Python 3
- No third-party Python packages required

The `requirements.txt` file is intentionally empty of package dependencies.

## Current Limitations

- Expenses are stored only while the program is running; they are not saved to a file or database.
- The amount input must be a valid number; invalid input can stop the program.
- The program does not currently support editing or deleting expenses.

## Future Improvements

- Save expenses in a CSV file or database.
- Add options to edit and delete expenses.
- Validate expense amounts and other inputs.
- Add monthly summaries and spending charts.

## Learning Outcomes

This project demonstrates fundamental Python concepts such as functions, lists, dictionaries, conditional statements, loops, and basic calculations.
