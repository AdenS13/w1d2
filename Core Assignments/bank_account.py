class BankAccount:

    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= amount - 5
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance *= self.interest_rate
            return self
        else:
            return self

jack = BankAccount(1.01, 0)
kevin = BankAccount(1.42, 250)

jack.deposit(500).deposit(500).deposit(500).withdraw(1000).yield_interest().display_account_info()
print(" ")
kevin.deposit(1500).deposit(2500).withdraw(250).withdraw(250).withdraw(250).withdraw(250).yield_interest().display_account_info()
        
