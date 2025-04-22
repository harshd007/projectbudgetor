# 📊 ProjectBudgetor

ProjectBudgetor is a simple and intuitive Python-based desktop application that helps you manage your project budgets and expenses efficiently. Built with **Tkinter**, it allows users to create projects, add expenses, view data in tabular format, and export it to CSV files.

---

## 🛠 Features

- ✅ Create multiple project budgets.
- ✅ Add categorized expenses with descriptions and date.
- ✅ View expenses in a tabular TreeView format.
- ✅ Prevent duplicate project names.
- ✅ Export project-specific expenses to CSV.
- ✅ Automatically saves data to a local JSON file.
- ✅ Clears input fields after data entry.
- ✅ GUI built using Tkinter.
- ✅ CSV files are saved directly to your Downloads folder.
- ✅ Button to clear the GUI window.

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ProjectBudgetor.git
cd ProjectBudgetor
```

### 2. Set Up Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# Activate virtualenv:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

> 📌 **Note**: This project uses only the Python standard library (like `tkinter`, `csv`, `json`, `os`, etc.), so you may not need external packages. If you face import issues, ensure you’re using **Python 3.8+**.

---

## 📂 Folder Structure

```
ProjectBudgetor/
│
├── gui/
│   └── app.py               # Main application file
│
├── models/
│   ├── project.py           # Project class
│   └── expense.py           # Expense class
│
├── data/
│   └── data.json            # Local storage for all data
│
├── README.md                # You're here!
└── requirements.txt         # Dependency list (optional)
```

---

## ▶️ Running the Application

Run the GUI:
```bash
python gui/app.py
```

---

## 📝 Usage Guide

1. **Create a Project**: Enter a project name and budget, then click "Create Project".
2. **Add Expenses**: Enter expense amount, category, and description. Click "Add Expense".
3. **Switch Between Projects**: Use the dropdown to view or switch projects.
4. **Export Data**: Click "Export Expenses to CSV" to save a file in your Downloads folder.
5. **Clear UI**: Use the "Clear Window" button to reset the display.

---

## 📤 Output

CSV files are exported to your system's **Downloads** folder with filenames like:
```
MyProject_expenses.csv
```

---

## 📦 Dependencies

- Python ≥ 3.8
- tkinter (comes with Python)
- json, csv, os, pathlib (all standard libraries)

---

## 💡 Future Ideas

- Add monthly budgeting graphs.
- Filter expenses by date or category.
- Add authentication for multi-user use.
- Dark mode UI toggle.

---

## 🙌 Contribution

Contributions, suggestions, or issue reports are welcome! Just fork the repo, make changes, and open a pull request.

---

## 📃 License

This project is open source and available under the MIT License.
