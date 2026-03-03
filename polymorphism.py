class BankAccount:
    def __init__(self,name,balance,loan):
        self.name = name         #public
        self._balance = balance #protected
        self.__loan = loan      #private
acc1 = BankAccount("Shubham",1_00_000, 5_00_000)
print(acc1.name,acc1._balance)
print(acc1._BankAccount__loan)   # Name mangling      