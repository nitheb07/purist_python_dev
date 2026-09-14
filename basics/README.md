# Python Basics

This folder contains examples for learning the core building blocks of Python programming.

## Getting Started

Install Python 3, then run these commands from the repository root:

```text
python basics/script1.py
python basics/script2.py
```

Or run them from this folder:

```text
python script1.py
python script2.py
```

`script2.py` asks for an integer. Try different values, including `0` and negative numbers, and observe the output.

## Course Topics

### 1. Print

Use `print()` to display text and values:

```python
print("Hello, Python!")
name = "Nitin"
print("Hello,", name)
```

### 2. Variables as Storage

A variable gives a name to a value:

```python
age = 25
temperature = 23.5
message = "Welcome"
is_ready = True
```

### 3. Math and Operators

```python
total = 10 + 3       # addition
difference = 10 - 3  # subtraction
product = 10 * 3     # multiplication
quotient = 10 / 3    # division
remainder = 10 % 3   # remainder
power = 2 ** 3       # exponent
```

Comparison operators return `True` or `False`:

```python
print(10 > 5)
print(10 == 5)
```

### 4. Interactive User Input

`input()` reads text typed by the user. Convert it when you need a number:

```python
name = input("What is your name? ")
age = int(input("How old are you? "))

print("Hello,", name)
print("Next year you will be", age + 1)
```

### 5. Logic and Conditionals

Use `if`, `elif`, and `else` to make decisions:

```python
temperature = 30

if temperature > 25:
    print("It is warm.")
elif temperature < 10:
    print("It is cold.")
else:
    print("The temperature is moderate.")
```

Logical operators include `and`, `or`, and `not`:

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You may enter.")
```

### 6. Lists: Grouped Data

A list stores multiple values in one variable. List indexes start at `0`:

```python
numbers = [10, 20, 30]

print(numbers[0])
numbers.append(40)
print(len(numbers))
```

`script2.py` also creates a list with `range()` and a list comprehension:

```python
limit = 20
numbers = [number for number in range(0, limit, 5)]
print(numbers)  # [0, 5, 10, 15]
```

### 7. Loops

Use a `for` loop to process each item in a list:

```python
for number in [10, 15, 20]:
    if number % 10 == 0:
        print(number)
```

Use a `while` loop while a condition is true:

```python
count = 3
while count > 0:
    print(count)
    count -= 1
```

## Example Files

| File | What it demonstrates |
| --- | --- |
| [`script1.py`](script1.py) | Variables, data types, output, arithmetic, and conditionals |
| [`script2.py`](script2.py) | User input, lists, functions, `for` loops, `while` loops, and logging |

## Practice Exercises

1. Change the values in `script1.py` and predict the output before running it.
2. Ask the user for two numbers and print their sum, difference, and product.
3. Create a list of five names and print each name with a `for` loop.
4. Ask for a number and print whether it is positive, negative, or zero.
5. Write a countdown that starts at a number entered by the user and ends at zero.

## Author

**Nitin Hebbar**  
Phone: +91-9735833538  
Email: [nit.hebbar18@gmail.com](mailto:nit.hebbar18@gmail.com)