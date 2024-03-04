class BudgetTracker:
    def _init_(self):
        self.expenses = []
        self.incomes = []

    def add_expense(self, amount, category, description):
        self.expenses.append({"amount": amount, "category": category, "description": description})

    def add_income(self, amount, category, description):
        self.incomes.append({"amount": amount, "category": category, "description": description})

    def total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)

    def total_incomes(self):
        return sum(income["amount"] for income in self.incomes)

    def show_expenses(self):
        for expense in self.expenses:
            print(expense)

    def show_incomes(self):
        for income in self.incomes:
            print(income)

# Sample usage
if __name__ == "_main_":
    tracker = BudgetTracker()
    tracker.add_expense(50, "Food", "Lunch")
    tracker.add_expense(30, "Transportation", "Bus fare")
    tracker.add_income(2000, "Salary", "Monthly paycheck")

    print("Total Expenses:", tracker.total_expenses())
    print("Total Incomes:", tracker.total_incomes())

    print("\nExpenses:")
    tracker.show_expenses()

    print("\nIncomes:")
    tracker.show_incomes()
