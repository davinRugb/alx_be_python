import sys

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")


def command_line_deposit(self):
     result = os.popen('python main-0.py deposit:50').read().strip()
     self.assertEqual(result, "Deposited: $50.00")

def command_line_withdraw(self):
    result = os.popen('python main-0.py withdraw:20').read().strip()
    self.assertEqual(result, "Withdrew: $20.00")

def command_line_withdraw_insufficient_funds(self):
     result = os.popen('python main-0.py withdraw:150').read().strip()
     self.assertEqual(result, "Insufficient funds.")

if __name__ == "__main__":
    main()
