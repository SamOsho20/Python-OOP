class Bank_Account:
    def __init__ (self,name, balance,int_rate):
        self.name = name
        self.balance = balance 
        self.int_rate = int_rate


    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"your balance is now {self.balance}")
        return self
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"your balance is now {self.balance}")
        return self
    def yield_interest(self, int_amount):
        self.balance = self.balance * (1 + int_amount)
        print(f"your balance with yeilded intrest is now {self.balance}")
        return self
    def display_account_info(self):
        print(f"{self.name},your current balance and is now {self.balance}")
        # we have now connected a variable that will track the user who is making transactions and  
        # give him/her back a comment  with their name and current balance 
        return self
    
account1 = Bank_Account("naomi",200,.01)
#creating 2 new instances 
account2 = Bank_Account("Bunmi",300,.01)
# account1.deposit(30).deposit(40).deposit(50).withdraw(20).yield_interest(.20)
# account2.deposit(40).deposit(50).withdraw(20).withdraw(50).withdraw(60).withdraw(30).yield_interest(.20)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bank_Account(name = name, int_rate=0.02, balance=0)

    def make_deposit(self,money_tracker):
        self.account.deposit(money_tracker)
    def make_withdrawal(self,money_tracker):
        self.account.withdraw(money_tracker)
    def display_user_balance(self, ):
        self.account.display_account_info()
    def transfer_money(self, amount, other_user):
        # to transfer money we need to enter 2 argumnets one being the amount that 
        # will be transfered and who it willl be transfered to.
        # knowing that we can use self we can use it to call out the account we are going to have transfer money to somebody 
        self.account.withdraw(amount)
        #we already have a method that subtracts the balance from the amount so lets call on it 

        other_user.make_deposit(amount)
        #we already have a method that adds  teh amount to balance so lets call on it 
        print(f"{self.name} deposited {amount} to {other_user.name}")
        # other_user.account.deposit would als work on line 46
        # we access timmys name using self.name to access teh account the money goes to rather than call it 
        # self.name, we call it other_user.name because other_user is 
        # a place value just like self to access atrributes in a a instance which is account 4 for sam


        
account3= User("sam", "samtheman@gamil.com")
account4= User("Timmy", "Timmyreads@gmail.com")
#we are creating multiple account  for the user that will and because our classes 
# are connected it will run through the methods in  the  above classes and print them when called
# print(account3.email)
# print(account4.email)
account3.make_deposit(1000)
account3.make_withdrawal(400)
account3.display_user_balance()
account4.make_deposit(2000)
account4.make_withdrawal(600)
account4.display_user_balance()
account4.transfer_money(100,account3)
#giving the transfer_money method 2 argumnents  it want so it can run


# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method 
# to the user class that takes an 
# amount and a different User instance, and 
# transfers money from the user's account into another user's account.

# take amount from account3 and transfers it into account4
# need 2 arguments



# account1.deposit(30).deposit(40).deposit(50).withdraw(20).yield_interest(.20)
# account2.deposit(40).deposit(50).withdraw(20).withdraw(50).withdraw(60).withdraw(30).yield_interest(.20)
# account1.display_account_info()
# account2.display_account_info()