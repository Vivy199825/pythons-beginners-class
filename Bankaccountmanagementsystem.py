class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount

    def display_transaction(self):
        print(f"Transaction Type: {self.transaction_type}, Amount: ${self.amount}")


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")

    def display_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            transaction.display_transaction()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction('Deposit', amount))
            print(f"Deposit successful. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction('Withdrawal', amount))
            print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount. Either the amount is zero or exceeds the available balance.")

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        self.transactions.append(Transaction('Interest', interest_amount))
        print(f"Interest applied. New balance: ${self.balance:.2f}")


# Error Handling Example:
try:
    account1 = BankAccount(account_number=1001, account_holder="John Doe")
    account1.deposit(-500)  # Invalid deposit amount
except ValueError as e:
    print(f"Error: {e}")

try:
    account1.withdraw(700)  # Invalid withdrawal amount (exceeds balance)
except ValueError as e:
    print(f"Error: {e}")