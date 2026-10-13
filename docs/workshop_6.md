# Workshop 6 — Functions, Part 2

## Prerequisites

- Workshop 2: `input()`, string methods, booleans
- Workshop 3: `if`/`elif`/`else`, `and`/`or`/`not`, `in`
- Workshop 4: `while`, `for`, `range`, `break`, `continue`
- Workshop 5: `def`, parameters, `return`, default values, scope,
  one function calling another

## 1. Keyword arguments

So far you passed arguments **by position**: the first value goes to
the first parameter, and so on. You can also pass them **by name**:

```python
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe("Nina", 25, "Tbilisi")
describe(city="Batumi", name="Luka", age=30)
# Nina, 25, from Tbilisi
# Luka, 30, from Batumi
```

With names, the order no longer matters, and the call explains itself.
Mix them freely, but **positional arguments come first**:

```python
describe("Nina", city="Kutaisi", age=25)
# Nina, 25, from Kutaisi
```

This pairs well with default values — skip the defaults you don't
care about and name the one you do:

```python
def make_tea(sugar=1, milk=False, lemon=False):
    print(f"sugar={sugar}, milk={milk}, lemon={lemon}")

make_tea(lemon=True)
# sugar=1, milk=False, lemon=True
```

## 2. Returning more than one value

`return` can send back several values separated by commas. The caller
unpacks them into several variables in one line:

```python
def min_max(a, b):
    if a < b:
        return a, b
    return b, a

smaller, bigger = min_max(9, 4)
print(smaller, bigger)
# 4 9
```

Python bundles the values into one object (a *tuple*) and unpacks it
on the other side. The number of variables on the left must match the
number of values returned.

## 3. Return early

`return` ends the function immediately (Workshop 5). That makes it a
clean way to handle special cases first, so the main code is not
buried in `else` blocks:

```python
def divide(a, b):
    if b == 0:
        return None
    return a / b

print(divide(10, 4))
print(divide(10, 0))
# 2.5
# None
```

The same trick works from inside a loop — **return the moment you
know the answer**:

```python
def first_even(limit):
    for n in range(1, limit + 1):
        if n % 2 == 0:
            return n
    return None

print(first_even(10))
print(first_even(1))
# 2
# None
```

If the loop finishes without returning, the code after it runs — here
it means "nothing found".

## 4. Local variables vs. global variables

A variable created **outside** every function is **global**. A
function can *read* it:

```python
tax_rate = 0.18

def with_tax(price):
    return price * (1 + tax_rate)

print(with_tax(100))
# 118.0
```

But assigning to a name inside a function creates a **new local
variable** — the global is left alone:

```python
count = 0

def add_one():
    count = count + 1   # UnboundLocalError

add_one()
```

To change a global you must say so with `global` (you saw this in
`khinkali.py`):

```python
herbs = 10

def use_herbs():
    global herbs
    herbs -= 1

use_herbs()
print(herbs)
# 9
```

It works, but **prefer parameters and `return`**. A function that
depends on a hidden global is hard to understand and hard to test:

```python
def use_herbs(herbs):
    return herbs - 1

herbs = use_herbs(herbs)
```

Everything the function needs comes in as parameters, and everything
it produces goes out through `return`.

## 5. Functions that answer yes/no

A function that returns `True` or `False` reads naturally in an `if`
or a `while`:

```python
def is_adult(age):
    return age >= 18

if is_adult(20):
    print("Welcome")
# Welcome
```

Return the comparison **directly** — no need for
`if age >= 18: return True else: return False`.

Name such functions like questions: `is_even`, `has_digit`,
`is_valid`.

## 6. Docstrings

A string on the first line inside a function documents it:

```python
def area(width, height):
    """Return the area of a rectangle."""
    return width * height
```

It is not executed; it tells the next reader (often you, next month)
what the function is for. Write one line saying what it **returns** or
**does**.

## 7. Putting it together: input validation

A function plus a `while` loop is the standard way to keep asking
until the user gives a good answer:

```python
def is_valid_password(password):
    """A valid password has 8+ characters and contains a digit."""
    if len(password) < 8:
        return False
    for ch in password:
        if ch in "0123456789":
            return True
    return False

def ask_password():
    while True:
        password = input("Choose a password: ")
        if is_valid_password(password):
            return password
        print("Too weak, try again.")

chosen = ask_password()
print("Password accepted.")
```

Notice how `return` inside `while True` is the way out — no `break`
needed — and how each function does one small job.

## Quick reference

| Idea | Example |
|------|---------|
| Keyword argument | `describe(name="Nina", age=25, city="Tbilisi")` |
| Return several values | `return a, b` / `x, y = f()` |
| Early return | `if b == 0: return None` |
| Change a global | `global herbs` (prefer parameters + `return`) |
| Yes/no function | `return age >= 18` |
| Docstring | `"""Return the area of a rectangle."""` |

## What's next

See `workshop_6/` for runnable examples, and your homework in
[python-127-homework-6](https://github.com/PythonADI/python-127-homework-6).
