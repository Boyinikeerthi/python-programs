#costum exception
class InsufficientBalanceError(Exception):
    def __init__(self,msg): #constructor
        super().__init__(msg)
class BankApp:
    def __init__(self,balance):
        self.balance=balance
    def Withdraw(self,amt):
        if self.balance<amt:
            raise InsufficientBalanceError("InsufficientBalance")
        else:
            print("Amount Withdrawn successflly")
bankapp=BankApp(10000)
try:
    bankapp.Withdraw(10000)
except InsufficientBalanceError as e:
    print(e)
