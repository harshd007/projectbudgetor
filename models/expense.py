from datetime import datetime

class Expense:
    def __init__(self, amount, description, category, date):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            "amount": self.amount,
            "description": self.description,
            "category": self.category,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Expense(data["amount"], data["description"], data["category"], data["date"])
