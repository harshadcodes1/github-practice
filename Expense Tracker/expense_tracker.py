#Mini Project - Expense Tracker#

import json


# Load expenses from JSON file
def load_data():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save expenses to JSON file
def save_data(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


# Add expense
def add_expense():

    expenses = load_data()

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    save_data(expenses)

    print("\nExpense added successfully!")


# View all expenses
def view_expenses():

    expenses = load_data()

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    print("\n========== ALL EXPENSES ==========")

    for i, expense in enumerate(expenses, start=1):

        print("\nExpense", i)
        print("Date        :", expense["date"])
        print("Category    :", expense["category"])
        print("Amount      : ₹", expense["amount"])
        print("Description :", expense["description"])


# Calculate total expense
def total_expense():

    expenses = load_data()

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Expense: ₹", total)


# Search by category
def search_category():

    expenses = load_data()

    category = input("Enter category to search: ")

    found = False

    print("\n========== SEARCH RESULT ==========")

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            print("Date        :", expense["date"])
            print("Amount      : ₹", expense["amount"])
            print("Description :", expense["description"])
            print("----------------------------")

            found = True

    if found == False:
        print("No expense found for this category.")


# Category-wise total
def category_summary():

    expenses = load_data()

    summary = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] = summary[category] + amount

        else:
            summary[category] = amount

    print("\n========== CATEGORY SUMMARY ==========")

    for category, amount in summary.items():

        print(category, ": ₹", amount)


# Delete expense
def delete_expense():

    expenses = load_data()

    if len(expenses) == 0:
        print("\nNo expenses available.")
        return

    view_expenses()

    number = int(input("\nEnter expense number to delete: "))

    if number >= 1 and number <= len(expenses):

        expenses.pop(number - 1)

        save_data(expenses)

        print("Expense deleted successfully!")

    else:
        print("Invalid expense number.")


# Main menu
while True:

    print("\n")
    print("================================")
    print("       EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Search by Category")
    print("5. Category Summary")
    print("6. Delete Expense")
    print("7. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        search_category()

    elif choice == "5":
        category_summary()

    elif choice == "6":
        delete_expense()

    elif choice == "7":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")