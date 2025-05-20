class Transaction:
    def payment(self, amount):
        self.amount = amount
        print("Transaction completed successfully:", self.amount)
class GooglePay(Transaction):
    def payment(self, amount):
        super().payment(amount)
        print("Paid via Google Pay.")
class CreditCard(Transaction):
    def payment(self, amount):
        super().payment(amount)
        print("Paid via Credit Card.")
class DebitCard(Transaction):
    def payment(self, amount):
        super().payment(amount)
        print("Paid via Debit Card.")
transaction = Transaction()
transaction.payment(1000)
googlepay = GooglePay()
googlepay.payment(2000)
creditcard = CreditCard()
creditcard.payment(5000)
debitcard = DebitCard()
debitcard.payment(4000)
