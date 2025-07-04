from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self,amount):
        self.amount= amount

    @abstractmethod
    def make_payment(self):
        pass

class CreditCard(Payment):
     def make_payment(self):
         print(f"made payment through credit card {self.amount}")

class DebitCard(Payment):
     def make_payment(self):
         print(f"made payment through debit card {self.amount}")

class UPIPayment(Payment):
    def make_payment(self):
        print(f"made payment through UPI {self.amount}")

payment= DebitCard(amount=100)
payment.make_payment()

payment= CreditCard(amount=500)
payment.make_payment()

