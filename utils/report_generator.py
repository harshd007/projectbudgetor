from tabulate import tabulate

def generate_report(project):
    print("\n--- Project Report ---")
    print(f"Project: {project.name}")
    print(f"Budget: ₹{project.budget}")
    print(f"Total Spent: ₹{project.total_spent()}")
    print(f"Remaining: ₹{project.remaining_budget()}")
    
    if not project.expenses:
        print("No expenses recorded.")
        return

    table = [[
        exp.date, exp.category, f"₹{exp.amount}", exp.description
    ] for exp in project.expenses]

    headers = ["Date", "Category", "Amount", "Description"]
    print("\nExpenses:\n")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
