# Workshop 8 — Dictionaries

## Prerequisites

- Workshop 3: `if`/`elif`/`else`, `in`
- Workshop 4: `for`, the accumulator, counting with a condition
- Workshop 5–6: `def`, `return`, returning several values
- Workshop 7: lists, indexing, `append`, looping over a list

## 1. Why dictionaries

A list finds things by **position**. To store a phone book with a
list, you would have to remember that Nina is at index 0:

```python
names = ["Nina", "Luka"]
phones = ["555-1234", "555-9876"]
print(phones[names.index("Luka")])
# 555-9876
```

A **dictionary** finds things by **key**. Each key is paired with a
value:

```python
phones = {"Nina": "555-1234", "Luka": "555-9876"}
print(phones["Luka"])
print(len(phones))
# 555-9876
# 2
```

Curly braces, `key: value` pairs, commas between the pairs. `{}` is an
empty dictionary. Keys are usually strings or numbers; values can be
anything — even lists.

## 2. Getting a value

Square brackets with the **key** instead of an index:

```python
ages = {"Nina": 19, "Luka": 22}
print(ages["Nina"])
# 19
```

Ask for a key that is not there and Python stops with an error:

```python
print(ages["Ana"])
# KeyError: 'Ana'
```

`.get()` returns `None` instead, or a default you choose:

```python
print(ages.get("Ana"))
print(ages.get("Ana", 0))
# None
# 0
```

And `in` asks whether a **key** is in the dictionary:

```python
print("Nina" in ages)
print(19 in ages)
# True
# False
```

`in` checks keys, not values — that is why `19 in ages` is `False`.

## 3. Adding, changing and removing

Assign to a key. If the key is new it is **added**; if it exists, its
value is **replaced**. A key can appear only once.

```python
ages = {"Nina": 19}
ages["Luka"] = 22      # add
ages["Nina"] = 20      # change
print(ages)
# {'Nina': 20, 'Luka': 22}
```

`pop(key)` removes a pair and returns its value, like `pop` on a list:

```python
removed = ages.pop("Luka")
print(removed, ages)
# 22 {'Nina': 20}
```

## 4. Looping over a dictionary

A `for` loop over a dictionary gives you the **keys**:

```python
prices = {"bread": 2.5, "milk": 3.0, "cheese": 9.0}
for item in prices:
    print(item, prices[item])
# bread 2.5
# milk 3.0
# cheese 9.0
```

`.items()` gives you the key **and** the value together — unpack them
into two variables, like returning several values in Workshop 6:

```python
total = 0
for item, price in prices.items():
    print(f"{item}: {price}")
    total += price
print(f"Total: {total}")
# bread: 2.5
# milk: 3.0
# cheese: 9.0
# Total: 14.5
```

`.keys()` and `.values()` give just one side.
`sum(prices.values())` is `14.5`.

## 5. Counting with a dictionary

The most common dictionary pattern: count how many times each thing
appears. Start empty; for each item, add 1 to its count — or start it
at 1 the first time you see it:

```python
words = ["cat", "dog", "cat", "bird", "cat"]
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
# {'cat': 3, 'dog': 1, 'bird': 1}
```

With `.get()` the `if` collapses into one line:

```python
counts[word] = counts.get(word, 0) + 1
```

## 6. Tuples

A **tuple** is like a list, but written with round brackets and it
**cannot be changed**:

```python
point = (3, 5)
print(point[0])
x, y = point
print(x + y)
# 3
# 8
```

```python
point[0] = 10
# TypeError: 'tuple' object does not support item assignment
```

You have already used tuples without knowing it: `return a, b` returns
a tuple, and `.items()` gives you `(key, value)` tuples.

## 7. Putting it together

A list of dictionaries is a tiny database:

```python
students = [
    {"name": "Nina", "score": 82},
    {"name": "Luka", "score": 95},
    {"name": "Ana", "score": 67},
]

def best(students):
    """Return the name of the student with the highest score."""
    top = students[0]
    for student in students:
        if student["score"] > top["score"]:
            top = student
    return top["name"]

print(best(students))
# Luka
```

## Quick reference

| Idea | Example |
|------|---------|
| Create | `ages = {"Nina": 19}` / `empty = {}` |
| Get | `ages["Nina"]`, `ages.get("Ana", 0)` |
| Has key? | `"Nina" in ages` |
| Add / change | `ages["Luka"] = 22` |
| Remove | `ages.pop("Luka")` |
| Loop keys | `for name in ages:` |
| Loop pairs | `for name, age in ages.items():` |
| One side | `ages.keys()`, `ages.values()` |
| Count | `counts[x] = counts.get(x, 0) + 1` |
| Tuple | `point = (3, 5)`, `x, y = point` |

## What's next

See `workshop_8/` for runnable examples, and your homework in
[python-127-homework-8](https://github.com/PythonADI/python-127-homework-8).
