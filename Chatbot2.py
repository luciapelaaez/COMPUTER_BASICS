from BankAccount2 import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, interest_rate):
        super().__init__(account_number)
        self.interest_rate = interest_rate

    def calculate_interest(self, years):
        interest = self.balance * (self.interest_rate / 100) * years
        return interest

print("Welcome to the Bank Account Chatbot!")
account_numbers = set()  # This is for making sure that the user cannot create an existing account, mostly for the section 8
accounts = {}  # This is like a dictionary for accounts in case the user wants more than one and wants to check each one.

# First, I will create a function that will create an account, making sure that the user enters 10 digits
# Also I will make sure that the account does not already exist (this will be useful later on for section 7)
def create_account():
    global account_numbers
    while True:
        account_number = input("Please enter your account number, which consists of ten digits: ")
        if len(account_number) == 10 and account_number.isdigit():
            if account_number in account_numbers:
                print("Sorry, this account already exists. Try with another number.")
            else:
                account_type = input("Enter 's' for savings account or 'c' for checking account: ").lower()
                if account_type == 's':
                    interest_rate = float(input("Enter the interest rate: "))
                    my_account = SavingsAccount(account_number, interest_rate)
                else:
                    my_account = BankAccount(account_number)
                account_numbers.add(account_number)
                accounts[account_number] = my_account
                print("Account created successfully!")
                print()
                input("Press Enter to return to the main menu.")
                break
        else:
            print("Error. You didn't enter ten digits. Please try again.")

    if my_account is None:
        print("Error: Account not created properly.")
        return  # Exit the function if account is not created

# Main menu loop
def main_menu(account_number):
    global accounts
    my_account = accounts[account_number]
    while True:
        print()
        print("1. Deposit money.")
        print("2. Withdraw money.")
        print("3. Check the account balance.")
        print("4. Help/tips for saving.")
        print("5. Transaction history.")
        print("6. Frequent questions (FAQ).")
        print("7. Create a new account.")
        print("8. Calculate interest (savings account).")
        print("9. Exit.")
        print()

        option = input("Please select an option by entering a number: ")

        if option == "1":
            amount = float(input("Please enter the amount you want to deposit or type 0 if you want to go back: "))
            if amount == 0:
                print("Operation cancelled. Returning to the main menu.")
                continue
            print(my_account.deposit(amount))
            print()
            input("Press Enter to return to the main menu.")
        elif option == "2":
            amount = float(input("Please enter the amount you want to withdraw or type 0 if you want to go back: "))
            if amount == 0:
                print("Operation cancelled. Returning to the main menu.")
                continue
            print(my_account.withdraw(amount))
            print()
            input("Press Enter to return to the main menu.")
        elif option == "3":
            print(f"Your current balance is {my_account.get_balance():.2f} €.")
            print()
            input("Press Enter to return to the main menu.")
        elif option == "4":
            print("Here are some tips you can apply for saving:")
            print()
            print("Tip 1. Set a Budget: Track your income and expenses to understand your spending habits.")
            print("Tip 2. Save Before You Spend: Automatically transfer a portion of your paycheck to savings.")
            print("Tip 3. Cook at Home: Prepare meals at home instead of eating out to save money.")
            print("Tip 4. Limit Impulse Purchases: Wait at least 24 hours before buying something you want but don’t need.")
            print("Tip 5. Set Savings Goals: Establish specific savings goals to motivate yourself.")
            print()
            input("Press Enter to return to the main menu.")
        elif option == "5":
            print("Transaction history:")
            for transaction in my_account.get_transaction_history():
                print(transaction)
            input("Press Enter to return to the main menu.")
        elif option == "6":
            print("1. What is a bank account? A bank account is a financial account maintained by a bank for a customer.")
            print("2. How do I create a new bank account in the chatbot? You can create a new bank account by entering your account number when prompted. Ensure it consists of ten digits.")
            print("3. What happens if I enter an invalid account number? If you enter an invalid account number that does not consist of ten digits, the chatbot will prompt you to try again.")
            print("4. Can I cancel a deposit or withdrawal operation? Yes, you can type '0' when prompted for an amount to cancel the operation and return to the main menu.")
            print("5. What happens if I try to withdraw more money than I have? If you attempt to withdraw more money than your current balance, the chatbot will inform you that you have insufficient funds.")
            print("6. How do I exit the chatbot? You can exit the chatbot by selecting the exit option from the menu.")
            print()
            input("Press Enter to return to the main menu.")
        elif option == "7":
            create_account()
            break
        elif option == "8":
            if isinstance(my_account, SavingsAccount):
                years = int(input("Enter the number of years to calculate interest: "))
                interest = my_account.calculate_interest(years)
                print(f"Interest for {years} year(s): {interest:.2f}€")
            else:
                print("This option is only available for savings accounts.")
            print()
            input("Press Enter to return to the main menu.")
        elif option == "9":
            print("Thank you for using the Bank Account Chatbot. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    while True:
        print("1. Create a new account")
        print("2. Access an existing account")
        print("3. Exit")
        main_option = input("Please select an option by entering a number: ")
        if main_option == "1":
            create_account()
        elif main_option == "2":
            account_number = input("Please enter your account number: ")
            if account_number in account_numbers:
                main_menu(account_number)
            else:
                print("Account not found. Please try again.")
                print()
        elif main_option == "3":
            print("Thank you for using the Bank Account Chatbot. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

