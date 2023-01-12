import random

class BankAccount():

    next_id = 1

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)
        self.id = BankAccount.next_id
        BankAccount.next_id += 1

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        print("\n Net Available Balance=",self.balance)
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=",self.balance)
        
    def __str__(self):
        return f' Account: {self.account_no} / Balance: {self.balance}'

    @classmethod
    def get_total_BankAccount(cls):
        return cls.next_id - 1

Wuilliam = BankAccount('Best babu', 50000)
print(Wuilliam)
print(Wuilliam)


Wuilliam.deposit()
Wuilliam.withdraw()
Wuilliam.display()











