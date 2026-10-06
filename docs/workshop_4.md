# Workshop 4 — Loops

## Prerequisites

- Workshop 1: variables, data types, type casting, f-strings, operators
- Workshop 2: `input()`, string methods, booleans, truthiness
- Workshop 3: `if`/`elif`/`else`, `and`/`or`/`not`, `in`, chained
  comparisons, conditional expressions

## 1. Why loops

Suppose you want to print three numbered lines. You could write three
`print()` calls — but then four lines means a fourth call, and a
hundred lines means a hundred. A loop lets you **repeat work without
repeating code**:

```python
count = 1
while count <= 3:
    print(f"Line {count}")
    count += 1
# Line 1
# Line 2
# Line 3
```

`while` means "as long as this condition is `True`, run the block
again". The condition is the same kind of condition you wrote in
Workshop 3.

## 2. The three parts of a `while` loop

Every working `while` loop has three parts: a **starting value**, a
**condition**, and a **change** that moves the condition toward
`False`:

```python
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Go!")
# 3
# 2
# 1
# Go!
```

- Starting value: `countdown = 3`
- Condition: `countdown > 0`
- Change: `countdown -= 1`

The `print("Go!")` is not indented, so it is outside the loop and runs
once, after the loop finishes.

## 3. The infinite loop

Forget the change and the condition never turns `False`:

```python
count = 1
while count <= 3:
    print(count)      # 1, forever — count never changes
# press Ctrl+C to stop it
```

`count` stays `1`, so `count <= 3` stays `True` and the loop never
ends. **If your program hangs and prints forever, press `Ctrl+C`** and
look for the missing change.

## 4. `for` and `range`

When you already know how many times to repeat, `for` with `range()`
says it more directly than `while`:

```python
for i in range(3):
    print(i)
# 0
# 1
# 2
```

`range(3)` produces the numbers `0`, `1`, `2`. The loop variable `i`
takes each of them in turn, and the block runs once per value. **You
don't manage the counter yourself** — there's no starting value to set
and no change to remember.

## 5. `range`'s three forms

| Call | Numbers produced |
|------|------------------|
| `range(5)` | `0 1 2 3 4` |
| `range(2, 6)` | `2 3 4 5` |
| `range(1, 10, 3)` | `1 4 7` |

With one argument it counts from `0`. With two it counts from the
first up to the second. With three, the last argument is the step.

**The stop value is always excluded.** `range(5)` stops before `5`, so
it gives five numbers starting at `0`. To count `1` to `3`, ask for
`range(1, 4)`:

```python
for number in range(1, 4):
    print(number)
# 1
# 2
# 3
```

## 6. `for` over a string

`for` isn't only for numbers. Given a string, **the loop variable takes
each character in turn**:

```python
for letter in "cat":
    print(letter)
# c
# a
# t
```

## 7. Accumulating a total

A variable created before the loop **survives across iterations**, so
you can build up a result:

```python
total = 0
for number in range(1, 5):
    total += number
    print(f"added {number}, total is now {total}")
print(f"Final total: {total}")
# added 1, total is now 1
# added 2, total is now 3
# added 3, total is now 6
# added 4, total is now 10
# Final total: 10
```

Note that `total = 0` is before the loop. Put it inside and it resets
to `0` on every pass, and the final answer is just the last number.

## 8. Counting with a condition inside the loop

Everything from Workshop 3 works inside a loop body. Here an `if`
decides whether this particular pass counts:

```python
vowels = 0
for letter in "programming":
    if letter in "aeiou":
        vowels += 1
print(f"vowels: {vowels}")
# vowels: 3
```

**The loop visits every character; the `if` chooses which ones matter.**

## 9. `break`

`break` **leaves the loop immediately**, skipping the remaining
iterations:

```python
for number in range(1, 10):
    if number == 4:
        break
    print(number)
print("done")
# 1
# 2
# 3
# done
```

`range(1, 10)` would have gone up to `9`, but the loop stops the first
time `number == 4`. Note that `4` is never printed — `break` happens
before the `print()`.

## 10. `continue`

`continue` **skips the rest of this pass and carries on with the
next** one:

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
# 1
# 2
# 4
# 5
```

The loop does not end — only `3` is missing. Keep the difference
clear: `break` ends the loop, `continue` ends one pass.

## 11. Nested loops

A loop body can contain another loop. **The inner loop runs fully for
every pass of the outer one**:

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} x {col} = {row * col}")
    print("---")
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ---
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# ---
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ---
```

The outer loop runs 3 times, the inner one 3 times per outer pass, so
the inner `print()` runs 9 times. The `print("---")` is indented at
the outer level, so it runs once per row.

## 12. `while` vs `for`

| Use | When |
|-----|------|
| `for` | You **know how many** repeats: a count, or every character of a string |
| `while` | You repeat **until something becomes true**, and can't say how many passes that takes |

Asking the user for input is the classic `while` case — you have no
idea how many attempts they will need:

```python
password = ""
while password != "python":
    password = input("Password: ").strip()
print("Welcome!")
```

`password = ""` before the loop makes the first check `False`, so the
loop runs at least once. The `input()` inside is the change that can
turn the condition `False`.

## What's next

See `workshop_4/` for runnable examples, and your homework in
[python-127-homework-4](https://github.com/PythonADI/python-127-homework-4).
