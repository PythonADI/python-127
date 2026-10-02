# Workshop 3 — Conditionals and Logical Operators

## Prerequisites

- Workshop 1: variables, data types, type casting, f-strings, operators
- Workshop 2: `input()`, string methods, booleans, truthiness

## 1. Making decisions

Every program so far ran top to bottom, executing every single line.
An `if` statement lets a program **choose** whether to run a block of
code, based on a condition:

```python
age = 20

if age >= 18:
    print("You may enter.")
```

The condition is `age >= 18`. As we saw in Workshop 2, a comparison
produces a `bool` — `True` or `False`. If it's `True`, the indented
block runs. If it's `False`, Python skips it entirely.

## 2. Indentation is the block

Most languages mark a block with `{` and `}`. Python uses
**indentation** — the spaces at the start of a line:

```python
age = 20

if age >= 18:
    print("You may enter.")      # inside the if
    print("Welcome!")            # also inside the if
print("Have a nice day.")        # outside — always runs
```

Two rules that Python enforces:

- The line with `if` ends with a **colon** `:`.
- Every line in the block is indented by the **same** amount. Use
  4 spaces — that's the convention the whole Python world follows.

Get either wrong and you get an error before your program even starts:

```python
if age >= 18
    print("hi")
# SyntaxError: expected ':'
```

```python
if age >= 18:
print("hi")
# IndentationError: expected an indented block after 'if' statement
```

## 3. `else`

`else` gives you the other path — it runs only when the condition was
`False`:

```python
age = 15

if age >= 18:
    print("You may enter.")
else:
    print("You are too young.")
```

Exactly one of the two blocks runs. Never both, never neither.

## 4. `elif`

To test several conditions in order, use `elif` ("else if"):

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

Python checks the conditions **top to bottom and stops at the first
`True` one**. `score = 75` is not `>= 90`, not `>= 80`, but it is
`>= 70` — so it prints `Grade: C` and never looks at the `else`.

This ordering matters. Written the other way around, every passing
score gets a `C`:

```python
score = 95

if score >= 70:
    print("Grade: C")      # this wins — 95 >= 70 is True
elif score >= 90:
    print("Grade: A")      # never reached
```

An `if` can have any number of `elif` branches, and the `else` is
optional.

## 5. `=` is not `==`

A single `=` **assigns**. A double `==` **compares**. Mixing them up is
the most common beginner mistake in any language:

```python
age = 20          # assignment: age now refers to 20
print(age == 20)  # comparison: True
```

Python protects you here — using `=` in a condition is a syntax error,
not a silent bug:

```python
if age = 20:
    print("hi")
# SyntaxError: invalid syntax. Maybe you meant '==' instead of '='?
```

## 6. Logical operators

To combine conditions, use `and`, `or`, and `not`:

| Operator | Result is `True` when... |
|----------|--------------------------|
| `a and b` | **both** `a` and `b` are `True` |
| `a or b` | **at least one** of `a`, `b` is `True` |
| `not a` | `a` is `False` |

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Enjoy the film.")

if age < 18 or not has_ticket:
    print("Sorry, you can't come in.")
```

The full truth table:

| `a` | `b` | `a and b` | `a or b` |
|-----|-----|-----------|----------|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

Note these are the words `and`, `or`, `not` — not `&&`, `||`, `!` as in
some other languages.

## 7. Each side needs a full condition

A very common mistake is writing a condition the way you'd say it out
loud:

```python
day = "saturday"

if day == "saturday" or "sunday":    # WRONG
    print("Weekend!")
```

This looks right and even seems to work — but it's always `True`, for
every day. Python reads it as `(day == "saturday") or ("sunday")`, and
`"sunday"` is a non-empty string, which is truthy (Workshop 2). So the
`or` always succeeds.

Spell out both comparisons:

```python
if day == "saturday" or day == "sunday":   # correct
    print("Weekend!")
```

## 8. Chaining comparisons

When you need a value to fall inside a range, Python lets you write the
comparison the way it looks in mathematics:

```python
temperature = 22

if 18 <= temperature <= 25:
    print("Comfortable.")
```

That means exactly the same as
`18 <= temperature and temperature <= 25`, just shorter.

## 9. Conditions don't have to be comparisons

An `if` accepts **any** value and applies the truthiness rules from
Workshop 2 — empty or zero is `False`, everything else is `True`:

```python
name = input("What is your name?\n").strip()

if name:
    print(f"Hello, {name}!")
else:
    print("You didn't type a name.")
```

If the user just pressed Enter, `name` is `""`, which is falsy, so the
`else` runs. Writing `if name:` is the idiomatic Python way to say
"if this isn't empty".

## 10. `in` — is this text inside that text?

For strings, `in` checks whether one piece of text appears inside
another. It produces a `bool`, so it works anywhere a condition does:

```python
email = input("Email: ").strip().lower()

if "@" in email:
    print("Looks like an email address.")
else:
    print("That's missing an @.")
```

`not in` is its opposite:

```python
if "@" not in email:
    print("That's missing an @.")
```

## 11. Nested conditions

An `if` block can contain another `if`. Indent the inner one one level
further:

```python
age = 25
has_ticket = False

if age >= 18:
    if has_ticket:
        print("Enjoy the film.")
    else:
        print("Please buy a ticket first.")
else:
    print("This film is 18+.")
```

Nesting gets hard to read quickly. When the inner condition is just
"and also this", prefer `and`:

```python
if age >= 18 and has_ticket:
    print("Enjoy the film.")
```

## 12. One-line conditional expressions

When you only need to **choose a value**, a conditional expression
(sometimes called a ternary) is more compact than four lines of
`if`/`else`:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)          # adult
```

Read it left to right: *the value is `"adult"` if `age >= 18`,
otherwise `"minor"`.* Use it for picking a value, not for running
several statements — an ordinary `if`/`else` is clearer for those.

## What's next

See `workshop_3/` for runnable examples, and your homework in
[python-127-homework-3](https://github.com/PythonADI/python-127-homework-3).
