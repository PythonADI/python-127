# Workshop 7 — Lists

## Prerequisites

- Workshop 2: strings, string methods, `len()`
- Workshop 3: `if`/`elif`/`else`, `in`
- Workshop 4: `for`, `range`, the accumulator, counting with a condition
- Workshop 5: `def`, parameters, `return`
- Workshop 6: keyword arguments, returning several values, early `return`

## 1. Why lists

Three test scores, three variables:

```python
score_1 = 90
score_2 = 75
score_3 = 82
```

Thirty students would need thirty variables. A **list** keeps many
values in one variable:

```python
scores = [90, 75, 82]
print(scores)
print(len(scores))
# [90, 75, 82]
# 3
```

Square brackets, commas between the items. `len()` — which you used
on strings — tells you how many items there are. A list can hold any
type, and `[]` is an empty list:

```python
names = ["Nina", "Luka", "Ana"]
empty = []
```

## 2. Indexing: getting one item

Every item has a position, its **index**. Indexes start at **0**,
just like `range(3)` gives `0, 1, 2`:

```python
names = ["Nina", "Luka", "Ana"]
print(names[0])
print(names[2])
print(names[-1])
# Nina
# Ana
# Ana
```

A **negative** index counts from the end: `-1` is the last item,
`-2` the one before it. The last positive index is always
`len(names) - 1`. Ask for an index that does not exist and Python
stops with an error:

```python
print(names[3])
# IndexError: list index out of range
```

## 3. Changing an item

Unlike a string, a list can be changed after it is created. Assign to
an index to replace that item:

```python
names = ["Nina", "Luka", "Ana"]
names[1] = "Giorgi"
print(names)
# ['Nina', 'Giorgi', 'Ana']
```

Notice that `print` shows the strings **with quotes** when they are
inside a list.

## 4. Adding and removing items

Lists have **methods**, called with a dot — like `.upper()` on a
string. The difference: list methods **change the list itself**.

```python
cart = ["bread", "milk"]
cart.append("cheese")
cart.insert(0, "water")
print(cart)
# ['water', 'bread', 'milk', 'cheese']

cart.remove("milk")
last = cart.pop()
print(last)
print(cart)
# cheese
# ['water', 'bread']
```

| Method | What it does |
|--------|--------------|
| `append(x)` | add `x` to the end |
| `insert(i, x)` | add `x` at index `i`, pushing the rest right |
| `remove(x)` | remove the first `x` (error if there is none) |
| `pop()` | remove the last item **and return it** |
| `pop(i)` | remove the item at index `i` and return it |

## 5. Looping over a list

`for` walks through a list item by item, exactly like it walked
through the letters of a string in Workshop 4:

```python
prices = [4.5, 12.0, 7.5]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
print(f"Average: {total / len(prices)}")
# Total: 24.0
# Average: 8.0
```

If you also need the **position**, loop over `range(len(...))` and
index into the list:

```python
names = ["Nina", "Luka", "Ana"]
for i in range(len(names)):
    print(i, names[i])
# 0 Nina
# 1 Luka
# 2 Ana
```

## 6. Building a list in a loop

Start with an empty list, `append` inside the loop, use it after. It
is the accumulator from Workshop 4 — but you collect values instead
of adding them up:

```python
evens = []
for n in range(1, 11):
    if n % 2 == 0:
        evens.append(n)
print(evens)
# [2, 4, 6, 8, 10]
```

## 7. Finding an element

`in` asks "is it there?" — you used it on strings in Workshop 3.
`.index()` gives the position of the **first** match, and `.count()`
says how many there are:

```python
fruits = ["apple", "pear", "plum", "pear"]
print("plum" in fruits)
print("kiwi" in fruits)
print(fruits.index("pear"))
print(fruits.count("pear"))
# True
# False
# 1
# 2
```

`.index()` stops with an error when the item is missing, so ask with
`in` first:

```python
if "kiwi" in fruits:
    print(fruits.index("kiwi"))
else:
    print("No kiwi.")
# No kiwi.
```

When the question is more than "is it equal?", search yourself — and
**return early** the moment you find it (Workshop 6):

```python
def first_over(numbers, limit):
    for n in numbers:
        if n > limit:
            return n
    return None

print(first_over([3, 8, 12, 5], 7))
print(first_over([3, 8, 12, 5], 20))
# 8
# None
```

## 8. Sorting

`sorted()` gives you a **new**, sorted list and leaves the original
alone. `reverse=True` — a keyword argument — sorts from biggest to
smallest:

```python
scores = [82, 95, 67, 90]
print(sorted(scores))
print(sorted(scores, reverse=True))
print(scores)
# [67, 82, 90, 95]
# [95, 90, 82, 67]
# [82, 95, 67, 90]
```

The method `.sort()` sorts **the list itself** and returns `None`:

```python
scores.sort()
print(scores)
# [67, 82, 90, 95]
```

So never write `scores = scores.sort()` — you would replace your list
with `None`:

```python
scores = scores.sort()
print(scores)
# None
```

Strings sort alphabetically: `sorted(["pear", "apple", "plum"])` is
`['apple', 'pear', 'plum']`.

## 9. `min`, `max`, `sum`

Three built-in functions answer the most common questions about a
list of numbers:

```python
scores = [82, 95, 67, 90]
print(min(scores), max(scores), sum(scores))
print(sum(scores) / len(scores))
# 67 95 334
# 83.5
```

## 10. Putting it together: functions that take a list

A list is passed to a function like any other value. Combine it with
returning several values:

```python
def summary(scores):
    """Return the lowest, highest and average score."""
    return min(scores), max(scores), sum(scores) / len(scores)

low, high, average = summary([82, 95, 67, 90])
print(f"Lowest {low}, highest {high}, average {average}")
# Lowest 67, highest 95, average 83.5
```

A function can also **build and return** a new list:

```python
def passed(scores, pass_mark=70):
    """Return a new list with only the passing scores."""
    result = []
    for score in scores:
        if score >= pass_mark:
            result.append(score)
    return result

print(passed([82, 95, 67, 90]))
print(passed([82, 95, 67, 90], pass_mark=85))
# [82, 95, 90]
# [95, 90]
```

## Quick reference

| Idea | Example |
|------|---------|
| Create | `scores = [90, 75, 82]` / `empty = []` |
| Length | `len(scores)` |
| Index | `scores[0]`, last: `scores[-1]` |
| Change an item | `scores[1] = 80` |
| Add | `append(x)`, `insert(i, x)` |
| Remove | `remove(x)`, `pop()`, `pop(i)` |
| Loop | `for score in scores:` |
| Build | `result = []` then `result.append(x)` in a loop |
| Find | `x in scores`, `scores.index(x)`, `scores.count(x)` |
| Sort | `sorted(scores)` (new list) / `scores.sort()` (in place) |
| Numbers | `min(scores)`, `max(scores)`, `sum(scores)` |

## What's next

See `workshop_7/` for runnable examples, and your homework in
[python-127-homework-7](https://github.com/PythonADI/python-127-homework-7).
