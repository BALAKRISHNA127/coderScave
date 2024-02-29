'''Create an app that simplifies expense sharing among friends or roommates. Users can input expenses, split 
bills, and track who owes whom'''


import csv

class Expense:
    def __init__(self, description, amount, paid_by, split_between):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.split_between = split_between

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open("expenses.csv", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                current_expense = None
                for row in reader:
                    if not current_expense or current_expense.description != row['Description']:
                        if current_expense:
                            self.expenses.append(current_expense)
                        current_expense = Expense(row['Description'], float(row['Amount']), row['PaidBy'], [])
                    current_expense.split_between.append(row['SplitBetween'])
                if current_expense:
                    self.expenses.append(current_expense)
        except FileNotFoundError:
            pass

    def save_expenses(self):
        with open("expenses.csv", "w", newline='') as csvfile:
            fieldnames = ['Description', 'Amount', 'PaidBy', 'SplitBetween']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                for participant in expense.split_between:
                    writer.writerow({'Description': expense.description, 'Amount': expense.amount, 'PaidBy': expense.paid_by, 'SplitBetween': participant})

    def add_expense(self, description, amount, paid_by, split_between):
        expense = Expense(description, amount, paid_by, split_between)
        self.expenses.append(expense)
        self.save_expenses()

    def calculate_owed_amounts(self):
        net_owed = {}
        for expense in self.expenses:
            share = expense.amount / len(expense.split_between)
            for person in expense.split_between:
                if person != expense.paid_by:
                    net_owed[person] = net_owed.get(person, 0) + share
                else:
                    net_owed[person] = net_owed.get(person, 0) - expense.amount + share
        return net_owed

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Calculate Owed Amounts")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3):")

        if choice == "1":
            description = input("Enter description  of (Items name) expense:")
            amount = float(input("Enter amount:$"))
            paid_by = input("Enter name of person who paid:")
            split_between = input("Enter names of persons to split (comma separated):").split(',')
            tracker.add_expense(description, amount, paid_by, split_between)
            print("Expense added successfully!")
        elif choice == "2":
            owed_amounts = tracker.calculate_owed_amounts()
            for person, amount in owed_amounts.items():
                if amount > 0:
                    print(f"{person} owes {abs(amount)}")
                elif amount < 0:
                    print(f"{person} is owed {abs(amount)}")
            if not owed_amounts:
                print("No expenses recorded yet.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
