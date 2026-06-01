class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print("Processing payment of:", self.amount)

class CreditCardPayment(Payment):
    pass
class UPIPayment(Payment):
    pass
p1=CreditCardPayment(500)
p1.pay()
p2=UPIPayment(300)
p2.pay()
