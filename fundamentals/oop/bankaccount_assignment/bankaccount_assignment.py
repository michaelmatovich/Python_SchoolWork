# Bank Account Assignment: Written by Michael J. Matovich

class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate/100
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    @classmethod
    def display_all_accounts(cls):
        print("Displaying All Account Information:")
        for account in cls.all_accounts:
            print(f"Balance: ${account.balance}, Interest Rate: {account.int_rate * 100}%")
        

# Instantiate 2 BankAccount objects
cloud = BankAccount(1)
sephiroth = BankAccount(5)

# Make 3 deposits, 1 withdrawal, yield interest, and display balance by chaining

cloud.deposit(50).deposit(100).deposit(50).withdraw(50).yield_interest().display_account_info()
print()

# Make 2 deposits, 4 withdrawals, yield interest, and display balance by chaining
sephiroth.deposit(5).deposit(10).withdraw(7).withdraw(8).withdraw(5).withdraw(10).yield_interest().display_account_info()
print()

# Use a class account to print all instances of a BankAccounts information

BankAccount.display_all_accounts()

