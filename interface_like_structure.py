from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def authenticate(self):
        """Authenticate the user"""
        pass

    @abstractmethod
    def payment_process(self, amount):
        """Process the payment"""
        pass

    @abstractmethod
    def generate_receipt(self):
        """Generate receipt"""
        pass

class Paypal(PaymentGateway):
    def authenticate(self):
        print("Authenticating the user with Paypal")

    def payment_process(self, amount):
       print(f"processing PayPal payment of ${amount}")

    def generate_receipt(self):
        print("Generating Paypal receipt..")

class Stripe(PaymentGateway):
    def authenticate(self):
        print("Authenticating the user with Stripe")

    def payment_process(self, amount):
        print(f"processing Stripe payment of ${amount}")

    def generate_receipt(self):
        print("Generating Stripe receipt..")

# Example Usage
paypal= Paypal()
paypal.authenticate()
paypal.payment_process(100)
paypal.generate_receipt()

stripe= Stripe()
stripe.authenticate()
stripe.payment_process(300)
stripe.generate_receipt()