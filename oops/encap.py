class BankAccount:
    def __init__(self,name,balance):
        self.name =name
        self.__balance = balance # private variable
    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid amount withdrawl ")

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("John", 10000)
#acc1.__balance = 2000 # direct access to private variable
# print(acc1.__balance)
print("Initial balance:", acc1.get_balance())
acc1.deposit(5000)
print("After deposit 5000:", acc1.get_balance())

acc1.withdraw(2000)
print("After withdraw 2000:", acc1.get_balance())

print(acc1.get_balance())

