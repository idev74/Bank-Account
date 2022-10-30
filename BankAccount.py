class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance = 0):
        self.full_name = full_name
        self.account_number = account_number
        self. routing_number = routing_number
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
        pass

    def add_interest(self):
        pass

    def print_receipt(self, full_name, account_number, routing_number, balance):
        print(f'{full_name} \nAccount No.: {account_number}\nRouting No.: {routing_number}\nBalance: ${balance}')
