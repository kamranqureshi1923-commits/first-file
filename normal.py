class Accouunt :
     def __init__(self,bal,acc):
         self.balance = bal
         self.account_no=acc
         
     #debit method
     def debit(self,amount):
         self.balance -= amount
         print("RS.",amount,"was debitade")
         print("total blance = ", self.get_balance())
         
     def credit(self,amount):
         self.balance += amount
         print("RS.",amount,"was creddited")
         print("total blance = ", self.get_balance())
         
     def get_balance(self):
         return self.balance   
         
         
acc1 = Accouunt(10000,12345)
acc1.debit(1000)
acc1.credit(600)
acc1.credit(50000)
acc1.debit(10000)