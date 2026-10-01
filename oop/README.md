# Python OOP: Object-Oriented Programming

Two beginner classes that build on the [`basics`](../basics/README.md) folder. You already know variables, `if`, lists, loops, and functions. Here you will learn to bundle them together into **objects**.

## Getting Started

Run from this folder:

```text
python class1_classes_objects.py
python class2_core_principles.py
```

Read each script from top to bottom, predict the output, then run it.

## How the Basics Map to OOP

| You already know | In OOP it becomes |
| --- | --- |
| Variables | Attributes (variables that belong to an object) |
| Functions | Methods (functions that belong to a class) |
| `if` / `elif` / `else` | Rules inside methods that control behavior |
| Lists and `for` loops | Lists of objects that you loop over |
| `if __name__ == "__main__":` | Still the entry point, same as `script2.py` |

---

# Class 1: Classes, Objects, and Methods

Script: [`class1_classes_objects.py`](class1_classes_objects.py)

### 1.1 The Problem

Imagine tracking a bank account with loose variables and functions:

```python
owner = "Asha"
balance = 100

def show_balance(owner: str, balance: float):
    print("%s has %.2f" % (owner, balance))
```

With ten accounts you would need twenty variables and you would always have to pass the right pair into every function. A class keeps the data and the functions together.

### 1.2 Class and Object

- A **class** is a blueprint. It describes what every account has and can do.
- An **object** (or **instance**) is one real thing built from that blueprint.

One blueprint for a house, many houses built from it.

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print("%s has %.2f" % (self.owner, self.balance))
```

### 1.3 The Key Words

| Term | Meaning |
| --- | --- |
| `class` | Starts a blueprint. Class names use `CapitalWords`. |
| `__init__` | Special method that runs automatically when an object is created. It sets up the starting data. |
| `self` | The object itself. Inside a method, `self.balance` means "the balance of this object". |
| Instance attribute | A variable stored on one object, such as `self.balance`. |
| Method | A function defined inside a class. |

### 1.4 Creating and Using Objects

```python
asha = BankAccount("Asha", 100)   # creates an object, runs __init__
ravi = BankAccount("Ravi")        # balance defaults to 0

asha.show_balance()               # call a method with a dot
print(ravi.balance)               # read an attribute with a dot
```

You do not pass `self` yourself. Python passes the object in front of the dot automatically.

Each object has its own data. Changing `asha.balance` does not change `ravi.balance`.

### 1.5 Function vs Method

| Standalone function | Method |
| --- | --- |
| Defined at the top level | Defined inside a class |
| Called as `show_balance(owner, balance)` | Called as `account.show_balance()` |
| Gets data only from its parameters | Can use the object's own data through `self` |

### 1.6 Conditionals Inside Methods

```python
def withdraw(self, amount: float):
    if amount > self.balance:
        print("Not enough money")
    else:
        self.balance -= amount
```

The object protects itself with the same `if` logic you already know.

### Guided Exercises (Class 1)

1. Run the script. Before you do, predict the final balance of `asha` and `ravi`.
2. Create a third account for yourself with a starting balance, deposit into it, and add it to the `accounts` list. Check the total.
3. Add a method `is_empty(self)` that returns `True` when the balance is `0`. Use it in an `if` statement.
4. Create a new class `Book` with attributes `title`, `pages`, and `pages_read` (starts at `0`). Add a method `read(self, count)` that adds to `pages_read` but never goes past `pages`. Add a method `progress(self)` that prints the percentage read.
5. Bonus: What happens if you forget `self` in `def show_balance():`? Try it and read the error.

---

# Class 2: Core OOP Principles

Script: [`class2_core_principles.py`](class2_core_principles.py)

Four big ideas. All four reuse the `BankAccount` from Class 1.

### 2.1 Encapsulation: Keep Data and Behavior Together

The account's data (`_balance`) and the rules that change it (`deposit`, `withdraw`) live in one class. Outside code asks the object to do things rather than editing its data directly.

```python
self.owner = owner       # public: fine to use directly
self._balance = balance  # internal: a leading underscore
```

**Python does not enforce privacy.** A single underscore is a convention that means "this is internal, please do not touch it". The script shows that `account._balance = 1000000` still works. Python trusts programmers to follow the convention. Following it keeps your rules (like "no negative balance") from being bypassed.

### 2.2 Inheritance: Reuse and Specialize

When a new class is a more specific kind of an existing class, inherit from it.

```python
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.05):
        super().__init__(owner, balance)   # reuse the parent setup
        self.rate = rate
```

- `SavingsAccount` gets `deposit`, `withdraw`, and `describe` for free.
- `super()` calls the parent's version of a method.
- A child can **override** a method by defining it again with the same name.

**When does inheritance make sense?** When you can say "a SavingsAccount **is a** BankAccount". If the sentence sounds wrong ("a Car is an Engine"), use a plain attribute instead ("a Car **has an** Engine").

### 2.3 Polymorphism: Same Call, Different Behavior

`month_end()` exists on every account, but each class does something different.

```python
for account in accounts:
    account.month_end()   # interest, fee, or nothing
```

The loop does not need `if` statements to check the account type. Each object knows what to do. Adding a new account type later does not require changing the loop.

### 2.4 Abstraction: Show What Is Needed, Hide the Rest

A user of `BankAccount` needs `deposit()`, `withdraw()`, and `describe()`. They do not need to know how the balance is stored or how the checks work. You already use abstraction every day: `print()` and `len()` hide how they work.

For now, treat abstraction as a design habit. Give a class a small, clear set of methods and keep the details inside. (Python has special syntax to force subclasses to provide certain methods. That is for a later class.)

### Guided Exercises (Class 2)

1. Run the script. Which line prints the broken balance, and why does Python allow it?
2. Change `rate` in `SavingsAccount("Ravi", 1200)` to `0.12`. Predict the new `month_end` result, then run it.
3. Create a `StudentAccount(BankAccount)` whose `withdraw` refuses any amount over `50`. Hint: check the amount, then call `super().withdraw(amount)`.
4. Add `StudentAccount` to the list in `demo_polymorphism`. Does the loop need to change?
5. Add a method `show_history(self)` to `BankAccount` that loops over `self._history` and prints each entry. Which principle is this an example of?

---

# Final Task: Student Grade Tracker

Reuse what you learned in both phases.

**Requirements**

1. Create a `Student` class with a `name` and a list of `grades` (starts empty).
2. Add `add_grade(self, grade)`. Only accept grades from `0` to `100`; otherwise print a message (conditionals).
3. Add `average(self)` using a `for` loop. Return `0` if there are no grades.
4. Add `status(self)` that returns `"pass"` when the average is at least `40`, otherwise `"fail"`.
5. Create `HonorsStudent(Student)` that needs an average of `60` to pass. Override only what you need.
6. In an `if __name__ == "__main__":` block, create a list holding one `Student` and one `HonorsStudent`. Use `input()` and a `while` loop to read grades for each student until the user types `-1`.
7. Loop over the list and print each student's name, average, and status. The loop must not check which kind of student it is.

**Checklist**

- [ ] Attributes hold the data (variables)
- [ ] Methods hold the behavior (functions)
- [ ] Conditionals guard `add_grade` and `status`
- [ ] Inheritance used for `HonorsStudent`
- [ ] Polymorphism: one loop, both student types

A sample solution is in [`final_task_solution.py`](final_task_solution.py). Try it yourself first.

## Example Files

| File | What it demonstrates |
| --- | --- |
| [`class1_classes_objects.py`](class1_classes_objects.py) | Classes, objects, `__init__`, `self`, attributes, methods |
| [`class2_core_principles.py`](class2_core_principles.py) | Encapsulation, inheritance, polymorphism, abstraction |
| [`final_task_solution.py`](final_task_solution.py) | Sample solution for the final task |

## Teaching Notes

- The examples use `%` formatting to match `script1.py` and `script2.py`. Introduce f-strings later.
- Suggested pacing: Class 1 is about 60 to 75 minutes. Class 2 is about 75 to 90 minutes. If time is short, move 2.3 and 2.4 into a third short session.
- Common mistakes to watch for: forgetting `self` as the first parameter, forgetting `self.` before an attribute, and expecting `_balance` to be truly private.
