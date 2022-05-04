# User Assignment. Written by Michael J. Matovich

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount	

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

# Instantiate 3 Users
larry = User("Larry", "Larry@3stooges.com")
curly = User("Curly", "Curly@3stooges.com")
moe = User("Moe", "Moe@3stooges.com")

# Check constructor init
print(f"{larry.name} - {larry.email} - {larry.account_balance}")
print(f"{curly.name} - {curly.email} - {curly.account_balance}")
print(f"{moe.name} - {moe.email} - {moe.account_balance}")
print()

# 3 deposits, 1 withdrawal and display balance
larry.make_deposit(100)
larry.make_deposit(200)
larry.make_deposit(300)
larry.make_withdrawal(50)
larry.display_user_balance()

# 2 deposits, 2 withdrawals and display balance
curly.make_deposit(500)
curly.make_deposit(400)
curly.make_withdrawal(100)
curly.make_withdrawal(150)
curly.display_user_balance()

# 1 deposit, 3 withdrawals and display balance
moe.make_deposit(5000)
moe.make_withdrawal(250)
moe.make_withdrawal(350)
moe.make_withdrawal(450)
moe.display_user_balance()

# Bonus: Transfer money from 1st user to 3rd user and display both balances
print()
larry.transfer_money(moe, 300)
larry.display_user_balance()
moe.display_user_balance()
