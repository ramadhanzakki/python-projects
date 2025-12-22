# Simple Money Tracker CLI

A lightweight command-line interface (CLI) application built with Python to help users manage their daily finances. This project implements **Object-Oriented Programming (OOP)** principles and uses **CSV** files for persistent data storage.

## 🚀 Features

- **Add Transactions**: Easily record income and expenses.
    
- **Persistent Storage**: All data is saved in a CSV file inside the `data/` folder.
    
- **Balance Tracking**: Real-time calculation of your current balance.
    
- **Financial Statistics**: View total income, total expenses, and a summary of your financial status.
    
- **Error Handling**: Basic validation for user inputs to prevent program crashes.
    

## 📁 Project Structure

```
MoneyTracker/
│
├── main.py              # Entry point of the application
├── data/
│   └── database.csv     # Data storage (auto-generated)
└── src/
    └── function.py      # Contains Transaction and Tracker classes
```

## 🛠️ Tech Stack

- **Language**: Python 3.13.3
    
- **Modules**: `csv`, `os`, `datetime`, `pathlib`
    
- **Storage**: CSV (Comma Separated Values)
    

## ⚙️ Installation & Usage

1. **Clone the repository** (or copy the project files):
    
    ```
    git clone [https://github.com/ramadhanzakki/python-projects/Money Tracker.git](https://github.com/ramadhanzakki/python-projects/Money Tracker.git)
    cd money-tracker-cli
    ```
    
2. **Run the application**:
    
    ```
    python main.py
    ```
    
3. **How to use**:
    
    - Select **Option 1** to add a new transaction.
	    
    - Choose between income or expenditure
        
    - Use **positive numbers** for Income and expenditure (e.g., `500`) 
        
    - Select **Option 2** to see your transaction history.
        
    - Select **Option 3** to see your financial summary.
        

## 📝 OOP Concepts Implemented

- **Classes & Objects**: Used `Transaction` for data modeling and `Tracker` for logic management.
    
- **Encapsulation**: Centralized file handling and data logic within the `Tracker` class.
    
- **Refactoring**: Improved code maintainability by separating concerns between classes.
    

## 👤 Author

- **Muhammad Zakki Fitra Ramadhan** - [Your GitHub Profile](https://github.com/ramadhanzakki "null")
    

_This project was created as part of a Python OOP learning journey._
