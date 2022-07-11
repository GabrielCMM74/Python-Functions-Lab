import random

class BankAccount():

    next_id = 1

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)
        self.id = BankAccount.next_id
        BankAccount.next_id += 1