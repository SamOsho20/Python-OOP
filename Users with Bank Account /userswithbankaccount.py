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
        # give him/her back a comnet with their name and current balance 
        return self
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
account1 = Bank_Account("naomi",200,.01)
account2 = Bank_Account("Bunmi",300,.01)
account3= User("sam", "samtheman@gamil.com")
account4= User("Timmy", "Timmyreads@gmail.com")
#we are creating multiple account  for the user that will and because our classes 
# are connected it will run through teh methods in  the  above classes and print them when called
# print(account3.email)
# print(account4.email)
account3.make_deposit(1000)
account3.make_withdrawal(400)
account3.display_user_balance()
account4.make_deposit(2000)
account4.make_withdrawal(600)
account4.display_user_balance()


# account1.deposit(30).deposit(40).deposit(50).withdraw(20).yield_interest(.20)
# account2.deposit(40).deposit(50).withdraw(20).withdraw(50).withdraw(60).withdraw(30).yield_interest(.20)
# account1.display_account_info()
# account2.display_account_info()