import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import pathlib 
import json
import csv
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.project import Project
from models.expense import Expense

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')

# Load and Save Functions
def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return [Project.from_dict(p) for p in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(projects):
    with open(DATA_FILE, 'w') as f:
        json.dump([p.to_dict() for p in projects], f, indent=4)

projects = load_data()

class BudgetorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ProjectBudgetor")

        self.project_name_var = tk.StringVar()
        self.budget_var = tk.StringVar()
        self.expense_amt_var = tk.StringVar()
        self.expense_desc_var = tk.StringVar()
        self.expense_cat_var = tk.StringVar()

        self.current_project = None

        self.build_ui()

    def build_ui(self):
        # Project Creation Section
        tk.Label(self.root, text="Project Name:").pack()
        tk.Entry(self.root, textvariable=self.project_name_var).pack()

        tk.Label(self.root, text="Budget:").pack()
        tk.Entry(self.root, textvariable=self.budget_var).pack()

        tk.Button(self.root, text="Create Project", command=self.create_project).pack(pady=5)

        # Expense Entry Section
        tk.Label(self.root, text="Expense Amount:").pack()
        tk.Entry(self.root, textvariable=self.expense_amt_var).pack()

        tk.Label(self.root, text="Category:").pack()
        tk.Entry(self.root, textvariable=self.expense_cat_var).pack()

        tk.Label(self.root, text="Description:").pack()
        tk.Entry(self.root, textvariable=self.expense_desc_var).pack()

        tk.Button(self.root, text="Add Expense", command=self.add_expense).pack(pady=5)
        tk.Button(self.root, text="Clear Window", command=self.clear_window).pack(pady=5)


        # Treeview to display expenses in tabular form
        self.tree = ttk.Treeview(self.root, columns=("Date", "Amount", "Category", "Description"), show="headings")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Description", text="Description")
        self.tree.pack(pady=10)

        # Dropdown to select a project
        tk.Label(self.root, text="Select a Project to View Expenses:").pack()
        self.project_selector = ttk.Combobox(self.root)
        self.project_selector.pack(pady=5)
        self.project_selector.bind("<<ComboboxSelected>>", self.on_project_select)

        # Button to show expenses for selected project
        tk.Button(self.root, text="Show Expenses", command=self.show_selected_project_expenses).pack(pady=5)

        # Button to export project expenses to CSV in tabular format
        tk.Button(self.root, text="Export Expenses to CSV", command=self.export_expenses_to_csv).pack(pady=5)

        # Initially update the dropdown list with available projects
        self.update_project_dropdown()

    def create_project(self):
        try:
            name = self.project_name_var.get()
            budget = float(self.budget_var.get())

            # Check if the project already exists
            if any(p.name == name for p in projects):
                messagebox.showerror("Error", "A project with this name already exists.")
                return

            self.current_project = Project(name, budget)
            projects.append(self.current_project)
            save_data(projects)
            messagebox.showinfo("Success", f"Created project '{name}' with ₹{budget} budget")
            self.update_project_dropdown()  # Update dropdown after project creation

            # Clear the project creation textboxes
            self.project_name_var.set("")
            self.budget_var.set("")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for budget")

    def add_expense(self):
        if not self.current_project:
            messagebox.showerror("Error", "No project selected.")
            return
        try:
            amount = float(self.expense_amt_var.get())
            desc = self.expense_desc_var.get()
            cat = self.expense_cat_var.get()
            date = datetime.now().strftime("%Y-%m-%d")
            self.current_project.add_expense(Expense(amount, desc, cat, date))
            self.update_expense_list()
            save_data(projects)

            # Clear the expense entry textboxes
            self.expense_amt_var.set("")
            self.expense_desc_var.set("")
            self.expense_cat_var.set("")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for expense amount")

    def update_expense_list(self):
        # Clear the current data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        if self.current_project:
            for e in self.current_project.expenses:
                self.tree.insert("", "end", values=(e.date, e.amount, e.category, e.description))

    def update_project_dropdown(self):
        # Refresh the project dropdown list
        self.project_selector['values'] = [p.name for p in projects]
        if self.current_project:
            self.project_selector.set(self.current_project.name)

    def on_project_select(self, event):
        selected_project_name = self.project_selector.get()
        self.current_project = next((p for p in projects if p.name == selected_project_name), None)
        self.update_expense_list()

    def show_selected_project_expenses(self):
        if not self.current_project:
            messagebox.showerror("Error", "No project selected.")
            return

        info = f"Expenses for Project: {self.current_project.name}\n"
        info += f"Budget: ₹{self.current_project.budget}\n\n"
        for e in self.current_project.expenses:
            info += f"{e.date} | ₹{e.amount} | {e.category} - {e.description}\n"
        
        messagebox.showinfo(f"Expenses for {self.current_project.name}", info)

    # def export_expenses_to_csv(self):
    #     if not self.current_project:
    #         messagebox.showerror("Error", "No project selected.")
    #         return

    #     file_name = f"{self.current_project.name}_expenses.csv"
    #     with open(file_name, mode='w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(["Date", "Amount", "Category", "Description"])  # CSV headers
    #         for expense in self.current_project.expenses:
    #             writer.writerow([expense.date, expense.amount, expense.category, expense.description])

    #     messagebox.showinfo("Success", f"Expenses data exported to {file_name}")
    
    def export_expenses_to_csv(self):
        if not self.current_project:
            messagebox.showerror("Error", "No project selected.")
            return

        # Get user's Downloads directory
        downloads_path = str(pathlib.Path.home() / "Downloads")
        file_name = f"{self.current_project.name}_expenses.csv"
        full_path = os.path.join(downloads_path, file_name)

        with open(full_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])  # CSV headers
            for expense in self.current_project.expenses:
                writer.writerow([expense.date, expense.amount, expense.category, expense.description])

        messagebox.showinfo("Success", f"Expenses data exported to:\n{full_path}")



    
    def clear_window(self):
        # Clear all input fields
        self.project_name_var.set("")
        self.budget_var.set("")
        self.expense_amt_var.set("")
        self.expense_desc_var.set("")
        self.expense_cat_var.set("")

        # Clear the expense table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Reset project selection
        self.project_selector.set("")
        self.current_project = None



if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetorApp(root)
    root.mainloop()


