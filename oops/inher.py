class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print("Processing payment of:", self.amount)

class CreditCardPayment(Payment):
    def pay(self):
        print("Processing credit card payment of:", self.amount,",+2% PF")
class UPIPayment(Payment):
    def pay(self):
        print("Processing UPI payment of:", self.amount,"With No Fee")
p1=CreditCardPayment(500)
p1.pay()
p2=UPIPayment(300)
p2.pay()

