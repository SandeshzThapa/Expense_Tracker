from expense_manager import ExpenseManager
from datetime import datetime

def main():
    manager = ExpenseManager()  # Create an instance of ExpenseManager
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Summary Report")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = datetime.now().strftime('%Y-%m-%d')
            amount = input("Enter amount: ")
            category = input("Enter category (e.g., food, transport): ")
            description = input("Enter description: ")
            manager.add_expense(date, amount, category, description)  # Add the expense
        elif choice == '2':
            manager.view_expenses()  # View all expenses
        elif choice == '3':
            manager.summary()  # Display summary of expenses
        elif choice == '4':
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
