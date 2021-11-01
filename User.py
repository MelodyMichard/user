class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
    
    def make_deposit(self, amount):
        self.amount += amount
    
    def make_withdrawal(self, amount):
        self.amount -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

guido = User("Guido van Rossum")
monty = User("Monty Python")
amy = User("Amy Pissue")

guido.make_deposit(150)
guido.make_deposit(200)
guido.make_deposit(550)
guido.make_withdrawal(600)
guido.display_user_balance()

monty.make_deposit(50)
monty.make_deposit(400)
monty.make_withdrawal(100)
monty.make_withdrawal(25)
monty.display_user_balance()

amy.make_deposit(1000)
amy.make_withdrawal(75)
amy.make_withdrawal(100)
amy.display_user_balance()


