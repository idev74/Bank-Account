import random

class BankAccount:
    def __init__(self, full_name, account_number = [], routing_number = 810273756, balance = 0):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: {amount}')

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
         print('Insufficient funds.')
         self.balance -= 10
        else:
            print(f'Amount Withdrawn: ${amount}')

    def get_balance(self):
        print(f'Your current balance is: {self.balance}')
        return self.balance

    def add_interest(self):
        interest = self.balance *  0.00083
        return interest

    def number_gen(self, account_number):
        for num in range(0, 8):
            account_number.append(random.randint(0,9))
        print(account_number)

    def print_receipt(self, full_name, account_number, routing_number, balance):
        print(f'{full_name} \nAccount No.: {account_number}\nRouting No.: {routing_number}\nBalance: ${balance}')



account1 = BankAccount('Hello Kitty')
print(account1)
