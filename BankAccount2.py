class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount:.2f}€")
            print(f"{amount:.2f}€ have been deposited correctly.")
        else:
            print("Deposit amount must be positive please.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew {amount:.2f}€")
                print(f"{amount:.2f}€ have been withdrew successfully.")
            else:
                print("Sorry, you have insufficient funds.")
        else:
            print("Withdraw amount must be positive please.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account number: {self.account_number}, balance: {self.balance:.2f} €"

    def get_transaction_history(self):
        return self.transaction_history

class SavingsAccount(BankAccount):
    def __init__(self, account_number, interest_rate):
        super().__init__(account_number)
        self.interest_rate = interest_rate

    def calculate_interest(self, years):
        interest = self.balance * (self.interest_rate / 100) * years
        return interest

class CheckingAccount(BankAccount):
    def __init__(self, account_number, overdraft_limit):
        super().__init__(account_number)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.balance + self.overdraft_limit >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew {amount:.2f}€")
                print(f"{amount:.2f}€ have been withdrew successfully.")
            else:
                print("Sorry, this exceeds your overdraft limit.")
        else:
            print("Withdraw amount must be positive please.")

# Examples
savings = SavingsAccount("0196745083", 1.5)
savings.deposit(1000)
print(f"Interest for 2 years: {savings.calculate_interest(2):.2f}€")
print(savings)

checking = CheckingAccount("1286745083", 500)
checking.deposit(300)
checking.withdraw(600)
checking.withdraw(900)
print(checking)
