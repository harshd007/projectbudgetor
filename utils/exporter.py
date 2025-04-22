import csv

def export_to_csv(project):
    filename = f"{project.name}_expenses.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for exp in project.expenses:
            writer.writerow([exp.date, exp.category, exp.amount, exp.description])
    print(f"Exported to {filename}")
