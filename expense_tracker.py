import json

# File to store expenses
EXPENSE_FILE = "expenses.json"

# Function to load expenses from file
def load_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense(expenses):
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., Food, Entertainment, etc.): ")
    date = input("Enter the date (YYYY-MM-DD): ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for expense in expenses:
            print(f"{expense['date']} - {expense['category']} - {expense['description']}: ${expense['amount']:.2f}")

# Function to calculate total expenses
def calculate_total_expenses(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total:.2f}")

# Main function
def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total_expenses(expenses)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
