"""
Class 2: Core OOP Principles
Encapsulation, Inheritance, Polymorphism, Abstraction

Run:  python class2_core_principles.py
"""


# ---------------------------------------------------------------
# 1. Encapsulation: keep data and the code that uses it together
# ---------------------------------------------------------------
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner            # public: fine to read and change
        self._balance = balance       # leading underscore: "internal, please don't touch"
        self._history = []            # also internal

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            self._history.append("deposit %.2f" % amount)

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._history.append("withdraw %.2f" % amount)
        else:
            print("Withdrawal refused: amount must be positive and not exceed the balance.")

    def month_end(self):
        """Hook that subclasses can change. The base account does nothing."""
        pass

    def describe(self) -> str:
        return "%s: %.2f" % (self.owner, self._balance)


def demo_encapsulation():
    print("--- Encapsulation ---")
    account = BankAccount("Asha", 100)
    account.withdraw(500)             # the rules inside the method protect the data
    print(account.describe())

    # Python does NOT block this. The underscore is only a convention
    # that tells other programmers "this is internal".
    account._balance = 1000000
    print("Broke the rules:", account.describe())


# ---------------------------------------------------------------
# 2. Inheritance: a specialised class built from a base class
# ---------------------------------------------------------------
class SavingsAccount(BankAccount):      # "is a" BankAccount
    def __init__(self, owner: str, balance: float = 0, rate: float = 0.05):
        super().__init__(owner, balance)    # reuse the parent's setup
        self.rate = rate                    # something new

    # Override: replace the parent's version of month_end.
    def month_end(self):
        interest = self._balance * self.rate / 12
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0, fee: float = 5):
        super().__init__(owner, balance)
        self.fee = fee

    def month_end(self):
        self.withdraw(self.fee)


def demo_inheritance():
    print("--- Inheritance ---")
    savings = SavingsAccount("Ravi", 1200)
    savings.deposit(100)              # deposit() was never written in SavingsAccount
    print(savings.describe())         # ...it is reused from BankAccount
    print("Is it a BankAccount?", isinstance(savings, BankAccount))


# ---------------------------------------------------------------
# 3. Polymorphism: same call, different behavior
# ---------------------------------------------------------------
def demo_polymorphism():
    print("--- Polymorphism ---")
    accounts = [
        BankAccount("Asha", 100),
        SavingsAccount("Ravi", 1200),
        CheckingAccount("Meena", 100),
    ]
    for account in accounts:
        account.month_end()           # one call, three different results
        print(account.describe())


# ---------------------------------------------------------------
# 4. Abstraction: use it without knowing how it works inside
# ---------------------------------------------------------------
def demo_abstraction():
    print("--- Abstraction ---")
    # We only need deposit(), withdraw() and describe().
    # We do not need to know about _balance, _history or the checks inside.
    account = CheckingAccount("Meena", 50)
    account.deposit(25)
    account.withdraw(10)
    print(account.describe())
    # The author of BankAccount could store money differently tomorrow
    # and this code would still work.


if __name__ == "__main__":
    demo_encapsulation()
    print()
    demo_inheritance()
    print()
    demo_polymorphism()
    print()
    demo_abstraction()
