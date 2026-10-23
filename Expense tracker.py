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
    print("Expense added successfully! ✅")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n===== EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - ₹{expense['amount']:.2f}")
        print(f"   {expense['description']}")


def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal expenses: ₹{total:.2f}")


def search_category():
    category = input("Enter category to search: ").lower()

    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(
                f"{expense['category']} - "
                f"₹{expense['amount']:.2f} - "
                f"{expense['description']}"
            )
            found = True

    if not found:
        print("No expenses found for that category.")


def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        number = int(input("Enter expense number to delete: "))
        removed = expenses.pop(number - 1)
        print(f"Deleted: {removed['description']} ✅")
    except (ValueError, IndexError):
        print("Invalid expense number.")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        search_category()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")
