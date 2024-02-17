class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category, month, year):
        self.expenses.append({'amount': amount, 'description': description, 'category': category, 'month': month, 'year': year})

    def monthly_summary(self, month, year):
        total_expenses = 0
        category_expenses = {}
        for expense in self.expenses:
            if expense['month'] == month and expense['year'] == year:
                total_expenses += expense['amount']
                if expense['category'] in category_expenses:
                    category_expenses[expense['category']] += expense['amount']
                else:
                    category_expenses[expense['category']] = expense['amount']
        return total_expenses, category_expenses

    def yearly_summary(self, year):
        total_expenses = 0
        month_category_expenses = {}
        for expense in self.expenses:
            if expense['year'] == year:
                month = expense['month']
                if month not in month_category_expenses:
                    month_category_expenses[month] = {'total': 0, 'categories': {}}
                month_category_expenses[month]['total'] += expense['amount']
                category = expense['category']
                if category not in month_category_expenses[month]['categories']:
                    month_category_expenses[month]['categories'][category] = 0
                month_category_expenses[month]['categories'][category] += expense['amount']
        total_expenses = sum(month_data['total'] for month_data in month_category_expenses.values())
        return total_expenses, month_category_expenses

    # def categorize_expenses(self):
    #     categories = set(expense['category'] for expense in self.expenses)
    #     return categories

    def user_interface(self):
        print("Welcome to Expense Tracker")
        while True:
            print("\n1. Add Expense\n2. View Monthly Summary\n3. View Yearly Summary\n4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_expense_interface()
            elif choice == '2':
                self.view_monthly_summary()
            elif choice == '3':
                self.view_yearly_summary()
            elif choice == '4':
                print("Thank you for using Expense Tracker!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_expense_interface(self):
        amount = float(input("Enter amount spent: "))
        description = input("Enter description: ")
        category = input("Enter category: ")
        month = input("Enter month (e.g., January): ").lower()
        year = input("Enter year: ")
        self.add_expense(amount, description, category, month, year)
        print("Expense added successfully!")

    def view_monthly_summary(self):
        month = input("Enter month (e.g., January): ").lower()
        year = input("Enter year: ")
        try:
            total_expenses, category_expenses = self.monthly_summary(month, year)
            print(f"Total expenses for {month.capitalize()} {year}: ${total_expenses}")
            print("Category-wise expenditure:")
            for category, amount in category_expenses.items():
                print(f"{category}: ${amount}")
        except KeyError:
            print("Invalid month or year entered.")

    def view_yearly_summary(self):
        year = input("Enter year: ")
        try:
            total_expenses, month_category_expenses = self.yearly_summary(year)
            print(f"Total expenses for the year {year}: ${total_expenses}")
            print("Month-wise expenditure:")
            for month, data in month_category_expenses.items():
                print(f"{month}:")
                print(f"Total: ${data['total']}")
                print("Category-wise expenditure:")
                for category, amount in data['categories'].items():
                    print(f"{category}: ${amount}")
        except KeyError:
            print("Invalid year entered.")

    # def view_category_wise_expenditure(self):
    #     categories = self.categorize_expenses()
    #     print("Available expense categories:")
    #     for category in categories:
    #         print(category)

if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    expense_tracker.user_interface()
