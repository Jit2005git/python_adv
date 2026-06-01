class Payment:
    def pay(self):
        print("Processing payment of:"self.amount)

class CreditCardPayment(Payment):
    pass
p1=CreditCardPayment()
p1.pay()
