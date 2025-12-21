import datetime
from src.function import Transaction, Tracker 


def main():
    # Welcome message
    print("===============================")
    print("   Welcome to Money Tracker   ")
    print("===============================\n")

    # displaying the amount of money saved
    tracker = Tracker()
    tracker.show_balance()

    # Main loop
    while True:
        # Menu options
        print("\nOptions:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Statistics")
        print("4. Exit")

        # User input
        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        # Handle user choices
        if choice == 1:
            print("Add Transaction selected.")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction = Transaction(date, amount, category, description)
            transaction.add_transaction()
            print("Transaction added successfully.")

        elif choice == 2:
            print("View Transactions selected.")
            transactions = tracker.load_transactions()
            if not transactions:
                print("No transactions found.")
            else:
                for t in transactions:
                    print(f"{t.date} | ${t.amount:.2f} | {t.category} | {t.description}")

        elif choice == 3:
            print("View Statistics selected.")
            # Expenses Total
            transactions = tracker.load_transactions()
            total_expenses = sum(t.amount for t in transactions if t.amount < 0)
            print(f"Total Expenses: ${total_expenses:.2f}")

            # Income Total
            total_income = sum(t.amount for t in transactions if t.amount > 0)
            print(f"Total Income: ${total_income:.2f}")

            # Balance
            balance = total_income + total_expenses
            print(f"Balance: ${balance:.2f}")

        elif choice == 4:
            print("Exiting Money Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()