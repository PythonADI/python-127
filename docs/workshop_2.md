# Workshop 2 — Input, Strings, and Booleans

## Prerequisites

- Workshop 1: variables, data types, type casting, f-strings, operators

## 1. Getting input from the user

So far every value in our programs was written directly in the code.
`input(...)` lets the **user** type a value while the program runs:

```python
name = input("What is your name?\n")
print(f"Hello, {name}!")
```

The text inside the parentheses is the **prompt** — it's printed first,
then the program waits until the user presses Enter. Whatever they typed
is returned and stored in `name`.

The prompt can be in any language:

```python
city = input("სად ცხოვრობ?\n")
```

## 2. `input()` always returns a `str`

Even if the user types `42`, `input()` gives you back the **text**
`"42"`, not the number `42`:

```python
age = input("How old are you?\n")
print(type(age))    # <class 'str'>
print(age + 1)      # TypeError: can only concatenate str (not "int") to str
```

## 3. Casting input

To do math with what the user typed, cast it — exactly like in
Workshop 1:

```python
age = int(input("How old are you?\n"))
print(f"In 5 years you will be {age + 5}.")
```

Use `float(...)` instead when the value can have a decimal point
(a price, a temperature, a height).

If the user types something that isn't a number (`"twenty"`), `int(...)`
raises a `ValueError`. We'll learn how to handle that later — for now,
type valid numbers when testing.

## 4. Strings and escape sequences

A string can use single or double quotes — both mean the same thing:

```python
first = 'Ada'
last = "Lovelace"
```

Inside a string, a backslash `\` starts an **escape sequence** — a
special character you can't easily type directly:

| Sequence | Meaning |
|----------|---------|
| `\n` | new line |
| `\t` | tab |
| `\"` | a double quote inside a `"..."` string |
| `\\` | a single backslash |

```python
print("Name:\tAda\nAge:\t25")
# Name:   Ada
# Age:    25
```

## 5. String methods

A **method** is a function that belongs to a value. You call it with a
dot after the value. Strings come with many useful methods:

```python
text = "   hello World   "

print(text.upper())    # "   HELLO WORLD   "
print(text.lower())    # "   hello world   "
print(text.strip())    # "hello World"  (spaces removed from both ends)
print(text.strip().title())  # "Hello World"
```

Methods **don't change** the original string — they return a new one.
To keep the result, assign it:

```python
name = input("Name: ").strip()
```

`len(...)` tells you how many characters a string has:

```python
print(len("Ada"))   # 3
```

## 6. Booleans

Every comparison produces a `bool` — either `True` or `False`:

```python
age = 20
is_adult = age >= 18
print(is_adult)          # True
print(type(is_adult))    # <class 'bool'>
```

A handy f-string trick: put `=` after an expression and Python prints
both the expression and its value:

```python
x = 10
print(f"{x > 5 = }")     # x > 5 = True
```

## 7. Truthiness

`bool(...)` converts any value to `True` or `False`. The rule is simple:
**empty or zero is `False`, everything else is `True`.**

```python
print(bool(0))        # False
print(bool(-5))       # True
print(bool(""))       # False  (empty string)
print(bool(" "))      # True   (a space is not empty!)
print(bool("0"))      # True   (a non-empty string, even if it says 0)
print(bool("False"))  # True   (same reason)
```

## 8. Floats aren't exact

Computers store decimal numbers in binary, so some values can't be
represented exactly:

```python
print(0.1 + 0.2)          # 0.30000000000000004
print(0.1 + 0.2 == 0.3)   # False
```

Use `round(value, digits)` to round to a fixed number of decimal places:

```python
print(round(0.1 + 0.2, 2))   # 0.3
print(round(3.14159, 2))     # 3.14
```

## 9. Constants

A **constant** is a variable that should never change after it's set.
Python doesn't enforce this — it's a **naming convention**: write the
name in `ALL_CAPS` to tell other programmers "don't reassign this".

```python
VAT_RATE = 0.18
price = 100
print(f"With VAT: {price * (1 + VAT_RATE)}")
```

## What's next

See `workshop_2/` for runnable examples, and your homework in
[python-127-homework-2](https://github.com/PythonADI/python-127-homework-2).
