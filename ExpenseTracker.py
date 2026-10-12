expenses = []


def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n===== All Expenses =====")

    for expense in expenses:
        print(
            "Category:", expense["category"],
            "| Amount:", expense["amount"],
            "| Description:", expense["description"]
        )
        

def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\nTotal Expenses:", total)


def category_summary():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n===== Category Summary =====")

    for category, amount in summary.items():
        print(category, ":", amount)


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        print("Thank you for using Expense Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")