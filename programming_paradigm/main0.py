# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command> [<amount>]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "deposit":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py deposit <amount>")
            sys.exit(1)
        try:
            amount = float(sys.argv[2])
            account.deposit(amount)
            print(f"Deposited ${amount:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    elif command == "withdraw":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py withdraw <amount>")
            sys.exit(1)
        try:
            amount = float(sys.argv[2])
            if account.withdraw(amount):
                print(f"Withdrew ${amount:.2f}")
            else:
                print("Withdrawal failed due to insufficient funds.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    elif command == "balance":
        account.display_balance()
    else:
        print(f"Unknown command: {command}")
        print("Valid commands are: deposit, withdraw, balance")

if __name__ == "__main__":
    main()
