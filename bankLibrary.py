class BankAccount:

    def __init__(self,account_number):
        self.account_number=account_number
        self.balance=0 
        self.transaction_history = []
    def deposit(self,amount):
        if amount>0:
            self.balance = self.balance + amount
            self.transaction_history.append(f"Deposited {amount:.2f}€") 
            print (f"{amount:.2f}€ have been deposited correctly.")
        else:
            print ("Deposit amount must be positive please.") 

       
    def withdraw(self,amount):
        if amount>0:
            if self.balance >= amount:
                self.balance = self.balance - amount
                self.transaction_history.append(f"Withdrew {amount:.2f}€")
                print (f"{amount:.2f}€ have been withdrew successfully")
            else:
                print ("Sorry, you have insufficient funds")
        else:
            print ("Withdraw amount must be positive please.")


    def get_balance (self):
        return self.balance

    def __str__(self):
        return f"Account number: {self.account_number}, balance: {self.balance:.2f} €"
    
    def get_trasnsaction_history (self):
        return self.transaction_history