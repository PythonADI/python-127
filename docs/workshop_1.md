# Workshop 1 — Getting Started with Python

## Prerequisites

- Python 3.12+ installed
- A text editor or IDE (VS Code, PyCharm, Sublime, or similar)

## 1. How does a computer work?

A computer runs on hardware (CPU, memory/RAM, storage) and software
(the instructions that tell the hardware what to do). The CPU repeats a
simple cycle millions of times per second:

1. **Fetch** — grab the next instruction from memory.
2. **Decode** — figure out what the instruction means.
3. **Execute** — carry it out.

Memory is organized into addressable bytes. Every value your program
uses — a number, a piece of text — lives at some memory address while
the program runs.

## 2. What is programming?

A computer only understands very simple instructions (add these two
numbers, compare these two values, jump to this instruction). Writing
useful software by hand in those terms would be unbearable, so we write
**source code** in a **programming language** — a language designed to
be readable by humans and translatable into instructions a computer can
run.

## 3. What is Python?

Python is a high-level, interpreted, general-purpose programming
language. "High-level" means it hides most hardware details from you.
"Interpreted" means your code is run directly by the Python interpreter
rather than compiled to machine code ahead of time.

## 4. Your first program

```python
print("Hello, World!")
```

`print(...)` writes text to the console. Anything after a `#` on a line
is a **comment** — the interpreter ignores it; it's there for humans.

```python
# This line prints a greeting
print("Hello, World!")
```

## 5. The console

The console (or terminal) is a text-based way to run programs, as
opposed to a GUI (graphical user interface) where you click buttons and
icons. Run a Python file from the console with:

```
python workshop_1/calc.py
```

## 6. Variables

A **variable** is a name that refers to a value stored in memory.

```python
age = 25
name = "Ada"
```

Here, `age` refers to a memory location holding `25`, and `name` refers
to a different location holding `"Ada"`. You can change what a variable
refers to at any time by assigning it again.

## 7. Data types

Every value in Python has a type. The core types you'll use constantly:

| Type | Meaning | Example |
|------|---------|---------|
| `int` | whole number | `42` |
| `float` | decimal number | `3.14` |
| `str` | text | `"hello"` |
| `bool` | true/false | `True` |

Check a value's type with `type(...)`:

```python
print(type(42))      # <class 'int'>
print(type(3.14))    # <class 'float'>
print(type("hi"))    # <class 'str'>
print(type(True))    # <class 'bool'>
```

## 8. Why data types matter

```python
age = 25
print("Age: " + age)
```

This raises `TypeError: can only concatenate str (not "int") to str`.
Python won't silently guess what you meant when combining a `str` and
an `int` with `+`. This is deliberate — it catches real bugs early.

## 9. Type casting

Convert between types explicitly with `int(...)`, `float(...)`, and
`str(...)`:

```python
age = 25
print("Age: " + str(age))   # works: both sides are now str
```

```python
text_number = "10"
print(int(text_number) + 5)  # 15
```

## 10. Operators

**Arithmetic:**

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | addition | `2 + 3` | `5` |
| `-` | subtraction | `5 - 2` | `3` |
| `*` | multiplication | `4 * 3` | `12` |
| `/` | division (always float) | `7 / 2` | `3.5` |
| `//` | floor division | `7 // 2` | `3` |
| `%` | modulo (remainder) | `7 % 2` | `1` |
| `**` | exponent | `2 ** 3` | `8` |

**Comparison** (all return a `bool`):

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | equal | `3 == 3` | `True` |
| `!=` | not equal | `3 != 4` | `True` |
| `>` | greater than | `5 > 2` | `True` |
| `<` | less than | `5 < 2` | `False` |
| `>=` | greater or equal | `5 >= 5` | `True` |
| `<=` | less or equal | `5 <= 2` | `False` |

## What's next

See `workshop_1/` for runnable examples, and your homework in
[python-127-homework-1](https://github.com/PythonADI/python-127-homework-1).
