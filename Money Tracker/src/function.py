import csv

class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    # Method to save transaction to CSV
    def add_transaction(self, filename='data/database.csv'):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.date, self.amount, self.category, self.description])

class Tracker:
    def __init__(self, filename='data/database.csv'):
        self.filename = filename

    # Method to load transactions from CSV
    def load_transactions(self):
        transactions = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    date, amount, category, description = row
                    transaction = Transaction(date, float(amount), category, description)
                    transactions.append(transaction)
        except FileNotFoundError:
            pass  # If file doesn't exist, return empty list
        return transactions

    # Method to show current balance
    def show_balance(self):
        transactions = self.load_transactions()
        balance = sum(t.amount for t in transactions)
        print(f"Current Balance: ${balance:.2f}")

    