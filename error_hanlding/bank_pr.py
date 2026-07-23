class InsufficientBalanceError(Exception):
    pass
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance in the account")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")
try:
    acc=BankAccount(1000)
    acc.withdraw(1500)
except InsufficientBalanceError as e:
    print("Transaction failed:", e)
    