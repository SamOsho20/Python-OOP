class Bank_Account:
    def __init__ (self,balance,int_rate):
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
        return self
        print(f"your balance with yeilded intrest is now {self.balance}")
    def display_account_info(self):
        print(f"your current balance and is now {self.balance}")
        return self
account1 = Bank_Account(200,.01)
account2 = Bank_Account(300,.01)

account1.deposit(30).deposit(40).deposit(50).withdraw(20).yield_interest(.20)
account2.deposit(40).deposit(50).withdraw(20).withdraw(50).withdraw(60).withdraw(30).yield_interest(.20)
account1.display_account_info()
account2.display_account_info()