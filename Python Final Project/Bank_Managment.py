
"""
    Project Name: Bank Managment System using Python with OOP
            Developed by: MD Shajjad Gani Shovon
                Student of Phitron Batch - 02
"""

class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_enabled = True

    def create_account(self, name, initial_balance):
        user = User(name, initial_balance)
        self.users.append(user)
        self.total_balance += initial_balance
        return user

    def admin_check_balance(self):
        return self.total_balance

    def admin_check_loan_amount(self):
        return self.total_loan_amount

    def Deactivate_loan_feature(self):
        self.loan_enabled = not self.loan_enabled

    def is_bankrupt(self):
        return self.total_balance < 0


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.loan_amount = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}BDT. Current balance: {self.balance}BDT"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount}BDT. Current balance: {self.balance}BDT"
        else:
            return "Insufficient funds. Unable to withdraw."

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            return f"Transferred {amount}BDT to {recipient.name}. Current balance: {self.balance}BDT"
        else:
            return "Insufficient funds. Unable to transfer."

    def check_balance(self):
        return f"Current balance: {self.balance}BDT"

    def take_loan(self):
        if Phitron_bank.loan_enabled:
            loan_amount = self.balance * 2
            self.loan_amount += loan_amount
            Phitron_bank.total_loan_amount += loan_amount
            Phitron_bank.total_balance -= loan_amount
            self.balance += loan_amount
            return f"Loan approved. Received {loan_amount}BDT. Current balance: {self.balance}BDT"
        else:
            return "Loan feature is currently disabled by the bank."

    def check_transaction_history(self):
        return self.transaction_history



Phitron_bank = Bank()

# Test Input for Checking:
user1 = Phitron_bank.create_account("Shajjad", 50000)
user2 = Phitron_bank.create_account("Shovon", 15500)

print(user1.deposit(5000))
print(user1.withdraw(2000))
print(user1.transfer(user2, 3000))
print(user1.check_balance())
print(user1.take_loan())

print("\nAdmin Actions:")
print(f"Total Bank Balance: ${Phitron_bank.admin_check_balance()}")
print(f"Total Loan Amount: ${Phitron_bank.admin_check_loan_amount()}")
print("Disabling Loan Feature.")
Phitron_bank.Deactivate_loan_feature()
print(user1.take_loan())

if Phitron_bank.is_bankrupt():
    print("The bank is bankrupt!")