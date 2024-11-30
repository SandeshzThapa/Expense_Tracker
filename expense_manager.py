import csv
from datetime import datetime

class ExpenseManager:
    def __init__(self, filename='data/expenses.csv'):
        self.filename = filename

    def add_expense(self, date, amount, category, description):
        # Open the CSV file and append data
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, category, description])
        print("Expense added successfully!")

    def view_expenses(self):
        try:
            # Read and display expenses from the CSV file
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                print("Date, Amount, Category, Description")
                for row in reader:
                    print(", ".join(row))
        except FileNotFoundError:
            print("No expenses found. Start by adding an expense.")

    def summary(self):
        try:
            total = 0
            category_totals = {}
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    amount = float(row[1])
                    category = row[2]
                    total += amount
                    if category in category_totals:
                        category_totals[category] += amount
                    else:
                        category_totals[category] = amount
            print(f"Total expenses: ${total:.2f}")
            for cat, amt in category_totals.items():
                print(f"{cat}: ${amt:.2f}")
        except FileNotFoundError:
            print("No expenses found. Start by adding an expense.")

