# Chaining Methods Assignment. Written by Michael J. Matovich

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

# Instantiate 3 Users
larry = User("Larry", "Larry@3stooges.com")
curly = User("Curly", "Curly@3stooges.com")
moe = User("Moe", "Moe@3stooges.com")

# Check constructor init
# print(f"{larry.name} - {larry.email} - {larry.account_balance}")
# print(f"{curly.name} - {curly.email} - {curly.account_balance}")
# print(f"{moe.name} - {moe.email} - {moe.account_balance}")
# print()

# 3 deposits, 1 withdrawal and display balance
larry.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

# 2 deposits, 2 withdrawals and display balance
curly.make_deposit(500).make_deposit(400).make_withdrawal(100).make_withdrawal(150).display_user_balance()

# 1 deposit, 3 withdrawals and display balance
moe.make_deposit(5000).make_withdrawal(250).make_withdrawal(350).make_withdrawal(450).display_user_balance()

# Bonus: Transfer money from 1st user to 3rd user and display both balances
print()
larry.transfer_money(moe, 300).display_user_balance()
moe.display_user_balance()
