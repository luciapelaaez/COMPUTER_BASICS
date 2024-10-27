class BankAccount:

    def __init__(self,account_number):
        self.account_number=account_number
        self.balance=0 #This variable says the money I have in my account, and by default it starts at zero
        self.transaction_history = [] #I will need this for the program or bankLibrary

    def deposit(self,amount):
        if amount>0:
            self.balance = self.balance + amount
            self.transaction_history.append(f"Deposited {amount:.2f}€")
            print (f"{amount:.2f}€ have been deposited correctly.")
        else:
            print ("Deposit amount must be positive please.") 
#I have defined that the money that I want to deposit in the account must be positive.
#Now the self.balance is not zero but is the amount that I want to put in my bank account.
       
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
#Now I have defined that the amount of money that I want to withdraw from the account must also be a positive number (I cannot withdraw -2 euros)
#If the current money in the account is less than the amount I want to withdraw, it means I don't have enough money in the account (I can't withdraw more money than I have)
#Likewise, if the amount I want to withdraw is less than the current amount of money in the account, then I can perform the withdrawal operation.       

    def get_balance (self):
        return self.balance
#With this, I establish the purpose of knowing the balance of my bank account so that after the result will be shown afterward.
#I also ensure that its value is not accidentally modified from outside the class.  
    
    def __str__(self):
        return f"Account number: {self.account_number}, balance: {self.balance:.2f} €"
#This is how I am representing a string of characters for when it is printed
    def get_transaction_history(self):
        return self.transaction_history



#To test that it works, I first create an instance of the class as I want.
my_account = BankAccount ("0196745083")
#Then, I'm adding money since my new account variable relates to the deposit method in my class.
my_account.deposit (23000)
#The same way, I'm withdrawing money in the next step.
my_account.withdraw (3800)
#Now I call my variable to display the final amount of money I have in the account.
print (f"Final balance of my account: {my_account.get_balance():.2f} €")
print () #I put this because I want a space after this
#I put () after the get.balance so that I execute the method of get.balance.

#Now I am going to provide another example to see if it works correctly with 2 decimal places by using :.2f.
my_account.deposit (1500.8945)
my_account.withdraw (200.987)
print (f"Updated balance of my account: {my_account.get_balance():.2f} €")
print ()

#Now I am doing another example in which I don't have enough money to withdraw to check if the program responds correctly.
another_account= BankAccount ("1286745083")
another_account.deposit (200)
another_account.withdraw (350)
print (f"The balance of this other account is: {another_account.get_balance():.2f} €")
