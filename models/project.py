from models.expense import Expense
class Project:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expenses(self):
        return sum(e.amount for e in self.expenses)

    def to_dict(self):
        return {
            "name": self.name,
            "budget": self.budget,
            "expenses": [e.to_dict() for e in self.expenses]
        }

    @staticmethod
    def from_dict(data):
        project = Project(data["name"], data["budget"])
        project.expenses = [Expense.from_dict(e) for e in data["expenses"]]
        return project
