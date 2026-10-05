
# 💰 Expense Tracker

## 📌 About the Project

**Expense Tracker** is a simple Python-based command-line application used to record and manage daily expenses.

The application stores expense data in a **JSON file** and provides different options to manage and analyze expenses.

## ✨ Features

* ➕ Add a new expense
* 👀 View all expenses
* 💰 Calculate total expenses
* 🔍 Search expenses by category
* 📊 View category-wise expense summary
* 🗑️ Delete an expense
* 💾 Store expense data permanently in a JSON file
* 🚪 Exit the application

## 🛠️ Technologies Used

* **Python**
* **JSON**
* **File Handling**
* **Functions**
* **Lists**
* **Dictionaries**
* **Loops**
* **Conditional Statements**

## 📂 Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
├── expenses.json
└── README.md
```

## 📋 Expense Information

Each expense contains the following information:

* **Date**
* **Category**
* **Amount**
* **Description**

Example:

```json
{
    "date": "26-08-2026",
    "category": "Food",
    "amount": 150.0,
    "description": "Lunch"
}
```

The project data file contains examples such as Food, Travel, and Shopping expenses.

## 🚀 Application Menu

When the program starts, it displays the following menu:

```text
================================
       EXPENSE TRACKER
================================
1. Add Expense
2. View Expenses
3. Total Expense
4. Search by Category
5. Category Summary
6. Delete Expense
7. Exit
================================
```

## ⚙️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

### Step 2: Open the Project Folder

Open the project folder in **VS Code** or Command Prompt.

### Step 3: Run the Program

```bash
python expense_tracker.py
```

### Step 4: Select an Option

Enter a number from **1 to 7** according to the operation you want to perform.

## 💾 Data Storage

The application uses Python's built-in `json` module to read and write expense data.

When a new expense is added, it is saved to the JSON file.

## 📊 Expense Management

### Total Expense

The application calculates the total amount of all stored expenses.

### Search by Category

Users can search for expenses by entering a category such as:

```text
Food
Travel
Shopping
```

The search is case-insensitive.

### Category Summary

The application calculates the total amount spent in each category.

### Delete Expense

Users can select an expense number and delete that expense from the stored data.

## 📚 Learning Outcomes

Through this project, I learned:

* Python programming
* Functions in Python
* Lists and dictionaries
* JSON file handling
* Reading and writing files
* User input handling
* Loops and conditional statements
* Searching and calculating data
* Building a menu-driven application
* Git and GitHub

## ⚠️ Note

This project is developed for **educational and learning purposes**.

## 👨‍💻 Author

**Harshad Jalindar Nikam**

Electronics & Computer Engineering

---

⭐ **If you find this project useful, feel free to star the repository!**
