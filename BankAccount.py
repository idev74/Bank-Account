class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self. routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        pass

    def add_interest(self):
        pass

    def print_receipt(full_name, account_number, routing_number, balance):
        print f'{full_name} \nAccount No.: {account_number}\nRouting No.: {routing_number}\nBalance: ${balance}'
