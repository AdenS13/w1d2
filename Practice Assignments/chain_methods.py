from unicodedata import name


class User:

    bank_name = "First National Dojo"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User:", self.name, "Balance:", self.account_balance)
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jack = User("Jack Sparrow", "jackys@gmail.com")

guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).display_user_balance()
print(" ")
monty.make_deposit(500).make_deposit(700).make_withdrawal(300).make_withdrawal(100).display_user_balance()
print(" ")
jack.make_deposit(100).make_withdrawal(33).make_withdrawal(33).make_withdrawal(33).display_user_balance()


