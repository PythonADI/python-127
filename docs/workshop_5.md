# Workshop 5 — Functions

## Prerequisites

- Workshop 1: variables, data types, type casting, f-strings, operators
- Workshop 2: `input()`, string methods, booleans, truthiness
- Workshop 3: `if`/`elif`/`else`, `and`/`or`/`not`, `in`, chained
  comparisons, conditional expressions
- Workshop 4: `while`, `for`, `range`, `break`, `continue`, nested loops

## 1. Why functions

You've already copy-pasted a block of code more than once. A function
lets you **name a block of code and run it by name**, instead of
retyping it:

```python
def greet():
    print("Hello!")
    print("Welcome to Python.")

greet()
greet()
# Hello!
# Welcome to Python.
# Hello!
# Welcome to Python.
```

`def greet():` **defines** the function — it does not run it. Nothing
is printed until `greet()` **calls** it, and you can call it as many
times as you like.

## 2. Parameters: feeding information in

A function that always does the exact same thing is limited.
**Parameters** let the caller pass in values:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Nina")
greet("Luka")
# Hello, Nina!
# Hello, Luka!
```

`name` is a parameter — a variable that only exists inside `greet`,
set to whatever was passed in each call. A function can take several:

```python
def greet(name, times):
    for _ in range(times):
        print(f"Hello, {name}!")

greet("Nina", 2)
# Hello, Nina!
# Hello, Nina!
```

## 3. `return`: sending a value back

`print()` shows something on screen; it doesn't give the rest of your
program a value to use. `return` **sends a value back to the caller**,
which you can store or use in an expression:

```python
def square(number):
    return number * number

result = square(4)
print(result)
# 16
```

**`return` immediately ends the function** — any code written after
it in the same call never runs:

```python
def check(number):
    if number < 0:
        return "negative"
    return "non-negative"

print(check(-3))
print(check(5))
# negative
# non-negative
```

## 4. Functions without `return`

A function with no `return` statement gives back `None`:

```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Nina")
print(result)
# Hello, Nina!
# None
```

`greet` prints as a side effect but doesn't hand anything back —
**`print()` and `return` solve different problems.** Use `return` when
the caller needs the value for something else.

## 5. Default parameter values

Give a parameter a default so the caller can **omit it**:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Nina")
greet("Luka", "Hi")
# Hello, Nina!
# Hi, Luka!
```

`greeting` falls back to `"Hello"` when the caller doesn't supply it.
A parameter with a default can be skipped; one without a default is
always required.

## 6. Scope: variables inside a function stay inside

A variable created inside a function **does not exist outside it**:

```python
def square(number):
    result = number * number
    return result

square(5)
print(result)
# NameError: name 'result' is not defined
```

`result` is **local** to `square` — created fresh each call and gone
once the function returns. This is also why a parameter named `name`
in one function doesn't clash with a variable named `name` elsewhere
in your program.

## 7. Calling functions from a loop

Workshop 4's loops and this workshop's functions combine directly —
call a function once per pass:

```python
def square(number):
    return number * number

for n in range(1, 5):
    print(f"{n} squared is {square(n)}")
# 1 squared is 1
# 2 squared is 4
# 3 squared is 9
# 4 squared is 16
```

## 8. One function calling another

A function body is ordinary code, so it can call other functions you
have already defined:

```python
def is_vowel(letter):
    return letter in "aeiou"

def count_vowels(word):
    total = 0
    for letter in word:
        if is_vowel(letter):
            total += 1
    return total

print(count_vowels("programming"))
# 3
```

`count_vowels` doesn't need to know *how* `is_vowel` decides — only
what it returns. **Breaking a problem into small functions that call
each other is easier to read and to test than one long block.**

## What's next

See `workshop_5/` for runnable examples, and your homework in
[python-127-homework-5](https://github.com/PythonADI/python-127-homework-5).
