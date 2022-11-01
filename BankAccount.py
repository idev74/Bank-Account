import random
import math

class BankAccount:
    def __init__(self, full_name, account_number = ['****'], routing_number = 810273756, balance = 0):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount}')

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
         print('Insufficient funds.')
         self.balance += amount - 10
        #  self.balance -= 10
        else:
            print(f'Amount Withdrawn: ${amount}')

    def get_balance(self):
        print(f'Your current balance is: {self.balance}')
        return self.balance

    def add_interest(self):
        interest = self.balance * 1.00083
        self.balance = math.floor(interest*100)/100

    def number_generator(self):
        for i in range(4):
            self.account_number.append(random.randint(0,9))
        self.account_number = (''.join(str(e) for e in self.account_number))
        # print(self.account_number)

    def print_receipt(self):
        print(f'{self.full_name} \nAccount No.: {self.account_number}\nRouting No.: {self.routing_number}\nBalance: ${self.balance}')



account1 = BankAccount('Hello Kitty')
account1.number_generator()
account1.deposit(100)
# account1.add_interest()
# account1.withdraw()
account1.print_receipt()