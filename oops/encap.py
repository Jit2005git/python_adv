class BankAccount:
    def init__(self,name,balance):
        self.name =name
        self.__balance = balance # private variable


acc1 = BankAccount("John", 1000)
#acc1.__balance = 2000 # direct access to private variable
print(acc1.__balance)
