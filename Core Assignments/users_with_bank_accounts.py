class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
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
            self.balance *= self.int_rate
            return self
        else:
            return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=1.02, balance=0)

jack = User("Jack", "jackys@gmail.com")
kevin = User("Kevin", "kevinzeigler@gmail.com")

jack.account.deposit(100).withdraw(25).yield_interest().display_account_info()
print(" ")
kevin.account.deposit(1500).deposit(2500).withdraw(250).withdraw(250).withdraw(250).withdraw(250).yield_interest().display_account_info()

