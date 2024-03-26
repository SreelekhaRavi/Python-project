class Bank:
    def __init__(self):
        self.Bank_accts= {}
 
    def create_account(self, account_number, account_holder, initial_balance):
        if account_number in self.Bank_accts:
            return "Account already exists"
        if initial_balance < 0:
            return "Balance is less than Zero"
 
        self.Bank_accts[account_number] = {'account_holder': account_holder,'balance': initial_balance}
        return "Account created successfully"
 
    def deposit(self, account_number, amount):
        if account_number not in self.Bank_accts:
            return "Invalid A/C number"
        if amount <= 0:
            return "Please deposit amount greater than Zero"
 
        self.Bank_accts[account_number]['balance'] += amount
        return "Deposited Amount : " + str(amount) + ". New balance : " + str(self.Bank_accts[account_number]['balance'])
 
    def withdraw(self, account_number, amount):
        if account_number not in self.Bank_accts:
            return "Account number not exist"
 
        if self.Bank_accts[account_number]['balance'] < amount:
            return "Insufficient balance."
 
        self.Bank_accts[account_number]['balance'] -= amount
        return "Withdrawal amount :  " + str(amount) + ". A/C balance : " + str(self.Bank_accts[account_number]['balance'])
 
    def check_balance(self, account_number):
        if account_number not in self.Bank_accts:
            return "Account number not exist"
 
        return "Account Holder : " + self.Bank_accts[account_number]['account_holder'] + "\nBalance : " + str(self.Bank_accts[account_number]['balance'])
 
bank = Bank() 
 
print("\n****** WELCOME TO XYZ BANK******")
print("\n1. New Account creation")
print("2. Deposit")
print("3. Withdrawal")
print("4. Check Balance Details")
print("5. Exit")
 
while True:
 
    choice = input("\nPlease select your option : ")
 
    if choice == '1':
        account_number = input("Enter Account Number : ")
        account_holder = input("Enter Account Holder's Name : ")
        initial_balance = float(input("Enter Initial Balance : "))
        accdetails = bank.create_account(account_number, account_holder, initial_balance)
        print(accdetails)
 
    elif choice == '2':
        account_number = input("Enter Account Number : ")
        amount = float(input("Enter Amount to Deposit : "))
        accdetails = bank.deposit(account_number, amount)
        print(accdetails)
 
    elif choice == '3':
        account_number = input("Enter Account Number : ")
        amount = float(input("Enter Amount to Withdraw : "))
        accdetails = bank.withdraw(account_number, amount)
        print(accdetails)
 
    elif choice == '4':
        account_number = input("Enter Account Number : ")
        accdetails = bank.check_balance(account_number)
        print(accdetails)
 
    elif choice == '5':
        print("Thank you!!!")
        break
 
    else:
        print("Invalid selection. Please Try Again !!!")