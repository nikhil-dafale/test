class Account:

    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("sorry, insufficient funds")

    def printstatement(self):
        print("Account balance is:", self.balance)


class Current(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{}Current acc balance is:{}".format(self.name, self.balance)


class Savings(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}Saving acc balance is:{}".format(self.name, self.balance)


x = Savings("nikhil", 10000)
print(x)

x.deposit(6000)
x.printstatement()
x.withdraw(19000)
x.withdraw(15999)
print(x)




