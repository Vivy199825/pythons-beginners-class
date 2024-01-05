class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, category, description, amount, payment_method):
        transaction = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount,
            'payment_method': payment_method
        }
        self.transactions.append(transaction)

    def calculate_total_expenses(self):
        total_expenses = sum(transaction['amount'] for transaction in self.transactions)
        return total_expenses

    def view_transactions(self):
        for transaction in self.transactions:
            print(f"Date: {transaction['date']}, Category: {transaction['category']}, "
                  f"Description: {transaction['description']}, Amount: ${transaction['amount']}, "
                  f"Payment Method: {transaction['payment_method']}")

# Example Usage:
expense_tracker = ExpenseTracker()

# Adding transactions
expense_tracker.add_transaction('2023-12-01', 'Groceries', 'Weekly grocery shopping', 50.00, 'Credit Card')
expense_tracker.add_transaction('2023-12-05', 'Entertainment', 'Movie night', 20.00, 'Cash')
expense_tracker.add_transaction('2023-12-10', 'Dining Out', 'Dinner with friends', 30.00, 'Debit Card')

# Viewing transactions
expense_tracker.view_transactions()

# Calculating total expenses
total_expenses = expense_tracker.calculate_total_expenses()
print(f"Total Expenses: ${total_expenses}")