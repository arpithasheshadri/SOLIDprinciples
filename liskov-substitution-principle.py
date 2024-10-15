# subtypes must be substitutable for their base types

# Let q(x) be a property provable about objects of x of type T. 
# Then q(y) should be provable for objects y of type S where S is a subtype of T.

# For example, if you have a piece of code that works with a Shape class, 
# then you should be able to substitute that class with any of its subclasses, 
# such as Circle or Rectangle, without breaking the code.

# LSP violation

# class Payment:
#     def process_payment(self,amount):
#         print(f"Processing the payment of {amount}")

# class CashPayment(Payment):
#     def process_payment(self, amount):
#         if amount > 1000:
#             raise ValueError("Cannot process cash payments above $1000.")
#         print(f"Processing the payment of {amount}")

# def makePayment(payment:Payment,amount):
#     payment.process_payment(amount)

# payment = Payment()
# payment.process_payment(1200)

# cashPayment = CashPayment()
# cashPayment.process_payment(1200)

#  Fixed LSP

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CashPayment(Payment):
    def process_payment(self, amount):
        if amount > 1000:
            raise ValueError("Cannot process cash payments above $1000.")
        print(f"Processing cash payment of ${amount}")

class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

def make_payment(payment:Payment, amount):
    payment.process_payment(amount)


cardPayment = CardPayment()
cardPayment.process_payment(1200)


cash_payment = CashPayment()
try:
    make_payment(cash_payment, 1200)  
except ValueError as e:
    print(e)