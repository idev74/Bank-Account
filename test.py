import random

# class BankAccount:
#     def __init__(self, account_number = ['****'], routing_number = 810273756):
#         self.account_number = account_number
#         self.routing_number = routing_number


# def number_gen(self):
#         for i in range(4):
#             self.account_number.append(random.randint(0,9))
#             print(self.account_number)

def numbers():
    a = ['****']
    for i in range(4):
        a.append(random.randint(0,9))
        # str(a)
        # ','.join(map(str,a))
    print(''.join(str(e) for e in a))
    # print(a)
    
numbers()