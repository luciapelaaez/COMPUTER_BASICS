from bankLibrary import BankAccount

print("Welcome to the Bank Account Chatbot!")
account_numbers = set () #This is for making sure that the user cannot create an existing account, mostly for the section 8
accounts = {} #This is like a dictionary for accounts in case the user wants more than one and wants to check each one.
#We use {} for an unordered list like the list of account and [] for ordered lists like the one of transaction history

#First, I will create a function that will create an account, making sure that the user enters 10 digits
#Also I will make sure that the account does not already exist (this will be useful later on for section 7)
def create_account():
    global account_numbers #Make sure is inside the chatbot so we can access and change it inside the chatbot
    #I create a loop so that the code block for creating the account is repeated as long as the condition that the user enters 10 digits is true
    while True:
        account_number = input("Please enter your account number, which consists of ten digits: ")
        if len(account_number) == 10 and account_number.isdigit(): #Make sure the user enters a number and that the number consists of 10 digits
            if account_number in account_numbers: #This condition checks if the account number has already been used to create an account
                print ("Sorry, this account already exits.Try with another number.") 
            else:
                my_account= BankAccount (account_number) #Create a new instance of the BankAccount class and assigning it to the variable my_account with the provided account number.
                account_numbers.add(account_number) #Add to the list of accounts number this new number account
                accounts[account_number] = my_account #Check that this new account now belongs to the list of all the global accounts
                print ("Account created successfully!")
                print ()
                input ("Press Enter to return to the main menu.") #Pause here 
                break #Because the function of creating an account is finished
        else:
            print("Error. You didn't enter ten digits. Please try again.")
    
    if my_account is None:
        print("Error: Account not created properly.")
        return  # Exit the function if account is not created

#Main menu loop
#With this new function the user will choose the options he/she wants
def main_menu (account_number):
    global accounts #Ensures the accounts dictionary can be accessed and modified inside the function.
    my_account = accounts[account_number] #So that all the users who has already created its account with a repesctive account number can access to this
    while True: 
        print()
        print("1. Deposit money.")
        print("2. Withdraw money.")
        print("3. Check the account balance.")
        print("4. Help/tips for saving.")
        print("5. Transaction history.")
        print("6. Frequent questions (FAQ).")
        print("7. Create a new account.")
        print("8. Exit.")
        print()

        option = input("Please select an option by entering a number: ")

        if option == "1":
            amount = float(input("Please enter the amount you want to deposit or type 0 if you want to go back: "))
            if amount == 0:
                print("Operation cancelled. Returning to the main menu.")
                continue #So that it skips the current iteration and returns to the top of the loop if the deposit is canceled.
            my_account.deposit(amount)
            print(f"Successfully deposited {amount:.2f} €.")
            print ()
            input("Press Enter to return to the main menu. ")  #Pause here
        elif option == "2":
            amount = float(input("Please enter the amount you want to withdraw or type 0 if you want to go back: "))
            if amount == 0:
                print("Operation cancelled. Returning to the main menu.")
                continue
            my_account.withdraw(amount)
            print(f"Successfully withdrew {amount:.2f} €.")
            print ()
            input("Press Enter to return to the main menu. ")  #Pause here
        elif option == "3":
            print(f"Your current balance is {my_account.get_balance():.2f} €.")
            print ()
            input("Press Enter to return to the main menu. ")  #Pause here
        elif option == "4":
            print("Here are some tips you can apply for saving:")
            print()
            print("Tip 1. Set a Budget: Track your income and expenses to understand your spending habits.")
            print("Tip 2. Save Before You Spend: Automatically transfer a portion of your paycheck to savings.")
            print("Tip 3. Cook at Home: Prepare meals at home instead of eating out to save money.")
            print("Tip 4. Limit Impulse Purchases: Wait at least 24 hours before buying something you want but don’t need.")
            print("Tip 5. Set Savings Goals: Establish specific savings goals to motivate yourself.")
            print ()
            input("Press Enter to return to the main menu. ")  #Pause here
        elif option == "5":
            print("Transaction history:")
            for transaction in my_account.transaction_history:  #So that it iterates through each transaction in the account's transaction history.
                print(transaction) #This will show all of the deposits and withdrwas realized on the user's account
            input("Press Enter to return to the main menu. ")  #Pause here
        elif option == "6":
            print("1. What is a bank account? A bank account is a financial account maintained by a bank for a customer.")
            print("2. How do I create a new bank account in the chatbot? You can create a new bank account by entering your account number when prompted. Ensure it consists of ten digits.")
            print("3. What happens if I enter an invalid account number? If you enter an invalid account number that does not consist of ten digits, the chatbot will prompt you to try again.")
            print("4. Can I cancel a deposit or withdrawal operation? Yes, you can type '0' when prompted for an amount to cancel the operation and return to the main menu.")
            print("5. What happens if I try to withdraw more money than I have? If you attempt to withdraw more money than your current balance, the chatbot will inform you that you have insufficient funds.")
            print("6. How do I exit the chatbot? You can exit the chatbot by selecting the exit option from the menu.")
            print ()
            input("Press Enter to return to the main menu. ")  #Pause here
        elif option == "8":
            print("Thank you for using the Bank Account Chatbot. Goodbye!")

        elif option =="7":
         create_account ()
         break
        else:
            print ("Invalid option. Please try again.") #In case the user didn't enter a number for 1 to 8, (the number of the options)
     
#This is what the user will see first on the screen
#The user can choose between ccreating an account, entering to an account which was created by the user before, or exit the program
if __name__ == "__main__":
    while True: #This loop will be repeated so that it's always what's seen on the screen
        print("1. Create a new account")
        print("2. Access an existing account")
        print("3. Exit")
        main_option = input("Please select an option by entering a number: ")
        if main_option == "1":
            create_account() #This option will take the user to the first function we have defined, that of creating an account.
        elif main_option == "2":
            account_number = input("Please enter your account number: ")
            if account_number in account_numbers: #Checks if the entered account number exists and then calls main_menu for that account if it does.
                main_menu(account_number) 
            else:
                print("Account not found. Please try again.") #This will take the user to the beginning of the loop so he/she can creates an account since the one he/she has set up doesn't exist
                print ()
        elif main_option == "3":
            print("Thank you for using the Bank Account Chatbot. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.") #In case the user didn't enter a number from 1 to 3
    