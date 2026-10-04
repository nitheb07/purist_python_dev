"""
Class 1: Classes, Objects, and Methods

Run:  python class1_classes_objects.py
"""


# ---------------------------------------------------------------
# Part 1: the old way - a standalone function and loose variables
# ---------------------------------------------------------------
def show_balance(owner: str, balance: float):
    """A standalone function: everything it needs must be passed in."""
    print("%s has %.2f" % (owner, balance))


# ---------------------------------------------------------------
# Part 2: the same idea as a class (a blueprint)
# ---------------------------------------------------------------
class BankAccount:
    """Blueprint for a bank account. Each account is one object."""

    # __init__ runs automatically when we create an object.
    # 'self' is the object being built; it is how the object refers to itself.
    def __init__(self, owner: str, balance: float = 0):
        # Instance attributes: variables that belong to ONE object.
        self.owner = owner
        self.balance = balance

    # Methods: functions defined inside a class.
    # The first parameter is always 'self'.
    def show_balance(self):
        print("%s has %.2f" % (self.owner, self.balance))

    def deposit(self, amount: float):
        # A conditional controls the method's behavior.
        if amount <= 0:
            print("Deposit must be more than 0.")
        else:
            self.balance += amount
            print("%s deposited %.2f" % (self.owner, amount))

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("%s: not enough money (balance %.2f)\n Please make more money" % (self.owner, self.balance))
        elif amount <= 0:
            print("Withdrawal must be more than 0.")
        else:
            self.balance -= amount
            print("%s withdrew %.2f" % (self.owner, amount))


def demo_function_vs_method():
    print("--- Function vs method ---")
    # Standalone function: we pass the data in ourselves.
    show_balance("Asha", 100)

    # Method: the object already holds its data. Called with a dot.
    account = BankAccount("Asha", 100)
    account.show_balance()


def demo_many_objects():
    print("--- Many objects from one class ---")
    # Each call to BankAccount(...) builds a NEW object.
    asha = BankAccount("Asha", 100)
    ravi = BankAccount("Ravi")          # balance uses the default, 0

    asha.deposit(50)
    ravi.deposit(20)
    ravi.withdraw(500)                  # too much - the if/elif blocks it
    asha.withdraw(30)

    # The objects keep separate data.
    asha.show_balance()
    ravi.show_balance()

    # Attributes can be read directly with a dot as well.
    print("Asha's balance attribute:", asha.balance)

    # Objects live happily in lists, and we can loop over them.
    accounts = [asha, ravi]
    total = 0
    for account in accounts:
        total += account.balance
    print("Total money in the bank: %.2f" % total)


if __name__ == "__main__":
    demo_function_vs_method()
    print()
    demo_many_objects()
