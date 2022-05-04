# Users with Bank Accounts Assignment: Written by Michael J. Matovich
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings = BankAccount(2)
        self.checking = BankAccount(0)

    def make_deposit(self, amount, account):	
        if(account == "savings"):
            self.savings.balance += amount
        else:
            self.checking.balance += amount

        return self

    def make_withdrawal(self,amount, account):
        if(account == "savings"):
            self.savings.balance -= amount
        else:
            self.checking.balance -= amount

        return self

    def display_user_balance(self, account):
        if(account == "savings"):
            print(f"User: {self.name}, Account: Savings Balance: ${self.savings.balance}")
        else:
            print(f"User: {self.name}, Account: Checking, Balance: ${self.checking.balance}")

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
        

cloud = User("Cloud", "spikyhair@omnislash.com")
sephiroth = User("Sephiroth", "psychoinferno@jenovahrocks.com")

cloud.make_deposit(100, 'savings')
cloud.display_user_balance('savings')
print()

sephiroth.make_deposit(1000, 'checking')
sephiroth.display_user_balance('checking')



