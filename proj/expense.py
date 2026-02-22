import json
import os

FILENAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    description = input("Enter expense description: ")
    amount = float(input("Enter amount: "))
    
    expense = {
        "description": description,
        "amount": amount
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!\n")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.\n")
        return
    
    print("\n📋 Expense List:")
    total = 0
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']} - ${expense['amount']:.2f}")
        total += expense['amount']
    
    print(f"\n💰 Total Spending: ${total:.2f}\n")


def main():
    expenses = load_expenses()
    
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()