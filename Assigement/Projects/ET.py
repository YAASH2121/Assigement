import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, category):
        today = datetime.date.today()
        if today not in self.expenses:
            self.expenses[today] = {}
        if category not in self.expenses[today]:
            self.expenses[today][category] = 0
        self.expenses[today][category] += amount

    def view_expenses(self):
        for date, categories in self.expenses.items():
            print(f"On {date}:")
            for category, amount in categories.items():
                print(f"- {category}: ${amount:.2f}")
            print()

    def total_spending(self):
        total = sum(sum(categories.values()) for categories in self.expenses.values())
        print(f"Total spending: ${total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. View Total Spending\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            tracker.add_expense(amount, category)
            print("Expense added successfully!")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.total_spending()
        elif choice == "4":
            print("Exiting...")
            print("Well come Again...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
