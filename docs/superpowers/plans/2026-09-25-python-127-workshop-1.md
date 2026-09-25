# python-127 Workshop 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build python-127's workshop 1 — course repo content (lesson, examples, slides) plus a javascript-205-style PR-based homework repo — and publish both to the `PythonADI` GitHub org.

**Architecture:** Two repos. `PythonADI/python-127` (this working directory) holds the lesson doc, example scripts, and slide deck. `PythonADI/python-127-homework-1` is a separate, self-contained repo students fork; it holds the exercises, a beginner-level Git/PR walkthrough, and the `CODEOWNERS`/PR-template machinery that auto-assigns the instructor as reviewer. Everything is authored locally first, verified, committed, then pushed to freshly created GitHub repos.

**Tech Stack:** Python 3.12+ (stdlib only, no dependencies), plain Markdown, a single self-contained HTML/CSS/JS file for slides (no CDN/build step), GitHub (via the `github` MCP tools) for repo creation and CODEOWNERS/PR-template mechanics.

**Spec:** `docs/superpowers/specs/2026-09-25-workshop-1-design.md`

## Global Constraints

- Target Python 3.12+; workshop 1 code may only use variables, data types (`int`/`float`/`str`/`bool`), type casting, and arithmetic/comparison operators — no loops, functions, or collections (not taught yet).
- Homework docs (`README.md`, `EXERCISES.md`, `SUBMITTING.md`, `submissions/README.md`) are bilingual: an English file plus a `_ka.md` Georgian counterpart.
- No CI/test automation anywhere — review is manual via `CODEOWNERS`.
- `.github/CODEOWNERS` in the homework repo contains exactly `* @tavkhelidzeluka`.
- PR title convention: `"Homework 1 - Your Name"`. Branch name convention: the student's GitHub username.
- Course repo: `PythonADI/python-127`. Homework repo: `PythonADI/python-127-homework-1`.
- Homework repo has no `.github/workflows/` — matches javascript-205 (no Actions anywhere in that org).

## Review Focus

- A student's reference solution output must exactly match what `EXERCISES.md` claims it prints — a copy-paste mismatch between the solution and the documented expected output would mislead every student grading their own work. Covered in Task 6.
- `SUBMITTING.md`'s commands must work for someone who has never opened a terminal before, on either Windows or macOS/Linux — a Mac-only `git` command example would strand Windows students (this instructor's own OS). Covered in Task 7.
- `.github/CODEOWNERS` must actually trigger an auto-requested review on a real PR — a wrong path or malformed syntax silently no-ops on GitHub. Covered in Task 9's end-to-end dry run.
- Exercise 2 ("fix a bug") needs the actual broken starter code inline in `EXERCISES.md`, not just a description of the bug — otherwise students can't reproduce the exact `TypeError` being taught. Covered in Task 6.
- Example scripts in `workshop_1/` must not accidentally use a loop, function, or collection (easy to slip in while writing a "realistic" demo) — verified by inspection in Task 3.

---

### Task 1: Course repo scaffolding

**Files:**
- Create: `README.md`
- Create: `docs/resources.md`

**Interfaces:**
- Produces: the course-repo README's workshop 1 row links to `docs/workshop_1.md`, `presentations/Workshop 1.html`, and `https://github.com/PythonADI/python-127-homework-1` (all three paths are fixed by this task and consumed by Tasks 2 and 4, which must land at those exact paths).

- [ ] **Step 1: Write `README.md`**

```markdown
# python-127

Beginner Python course. Each workshop has a lesson doc, a slide deck, and a
separate homework repo submitted via Pull Request.

## Workshops

| # | Lesson | Slides | Homework |
|---|--------|--------|----------|
| 1 | [Workshop 1](docs/workshop_1.md) | [Slides](presentations/Workshop%201.html) | [python-127-homework-1](https://github.com/PythonADI/python-127-homework-1) |

## Resources

See [docs/resources.md](docs/resources.md) for recommended reading.

## Requirements

- Python 3.12+
- A text editor or IDE (VS Code, PyCharm, or similar)
```

- [ ] **Step 2: Write `docs/resources.md`**

```markdown
# Resources

- [Python Crash Course, 3rd Edition](https://nostarch.com/python-crash-course-3rd-edition) — the core text for this course.
- [Official Python Tutorial](https://docs.python.org/3/tutorial/) — free, official, and thorough.
- [Real Python](https://realpython.com/) — free articles and tutorials on specific topics.
```

- [ ] **Step 3: Verify links resolve to files this plan will create**

Confirm `docs/workshop_1.md` (Task 2), `presentations/Workshop 1.html` (Task 4), and `workshop_1/` (Task 3) match the paths referenced in `README.md` exactly, including the space in `Workshop 1.html` (URL-encoded as `%20` in the Markdown link).

- [ ] **Step 4: Commit**

```bash
git add README.md docs/resources.md
git commit -m "Add course repo scaffolding"
```

---

### Task 2: Workshop 1 lesson doc

**Files:**
- Create: `docs/workshop_1.md`

**Interfaces:**
- Consumes: nothing.
- Produces: the lesson content that `workshop_1/` example scripts (Task 3) and `presentations/Workshop 1.html` (Task 4) must stay consistent with (same topic order, same terminology).

- [ ] **Step 1: Write `docs/workshop_1.md`**

```markdown
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
```

- [ ] **Step 2: Verify every code sample in the doc is copy-paste runnable**

Extract each fenced ` ```python ` block and run it with `python3 -c` (or paste into a scratch `.py` file and run with `python workshop_1/_scratch.py`); confirm the shown output matches what actually prints, then delete the scratch file. The `TypeError` example (step 8) should raise exactly `TypeError: can only concatenate str (not "int") to str` — confirm the wording rather than assuming it.

- [ ] **Step 3: Commit**

```bash
git add docs/workshop_1.md
git commit -m "Add workshop 1 lesson doc"
```

---

### Task 3: Workshop 1 example scripts

**Files:**
- Create: `workshop_1/calc.py`
- Create: `workshop_1/main.py`

**Interfaces:**
- Consumes: the concepts and terminology from `docs/workshop_1.md` (Task 2) — the scripts must not use anything beyond variables/types/casting/operators.
- Produces: nothing consumed by later tasks; these are standalone runnable demos.

- [ ] **Step 1: Write `workshop_1/calc.py`**

```python
# A tiny receipt calculator using only variables, types, and operators.

item = "Coffee"
price = 4.5
quantity = 3

total = price * quantity

print(f"Item: {item}")
print(f"Price: {price} GEL")
print(f"Quantity: {quantity}")
print(f"Total: {total} GEL")
```

- [ ] **Step 2: Run it and record the exact output**

```
python workshop_1/calc.py
```

Expected:
```
Item: Coffee
Price: 4.5 GEL
Quantity: 3
Total: 13.5 GEL
```

- [ ] **Step 3: Write `workshop_1/main.py`**

```python
# Grab-bag demo: types, casting, and operators.

print(type(10))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

print(10 % 3)             # 1
print(10 // 3)             # 3
print(2 ** 10)             # 1024

age = 25
# age + "3" would raise TypeError: cast first
age_text = str(age) + "3"
print(age_text)            # "253" (string concatenation, not addition)

big_number = 7 ** 1000
print(type(big_number))    # <class 'int'> — Python ints have no fixed size
```

- [ ] **Step 4: Run it and record the exact output**

```
python workshop_1/main.py
```

Expected: the six values above (`<class 'int'>`, `<class 'float'>`,
`<class 'str'>`, `<class 'bool'>`, `1`, `3`, `1024`, `253`,
`<class 'int'>`) in that order, with `7 ** 1000` printing a very long
digit string on the line before its type is printed — this is a
deliberate example of Python's arbitrary-precision integers, not an
error.

- [ ] **Step 5: Inspect both files for scope creep**

Confirm neither file contains a loop (`for`/`while`), a function
definition (`def`), or a collection literal (`[]`, `{}`, `()` used as a
tuple) — workshop 1 hasn't taught those yet.

- [ ] **Step 6: Commit**

```bash
git add workshop_1/calc.py workshop_1/main.py
git commit -m "Add workshop 1 example scripts"
```

---

### Task 4: Workshop 1 slide deck

**Files:**
- Create: `presentations/Workshop 1.html`

**Interfaces:**
- Consumes: the section order and terminology from `docs/workshop_1.md` (Task 2) — slides should follow the same ten sections.
- Produces: nothing consumed by later tasks.

- [ ] **Step 1: Write `presentations/Workshop 1.html`**

A single self-contained HTML file (inline `<style>` and `<script>`, no
external requests) with one `<section class="slide">` per lesson topic
from `docs/workshop_1.md` (title slide, how computers work, what is
programming, what is Python, first program, console, variables, data
types, why types matter, type casting, operators, wrap-up — 12 slides
total), arrow-key and click navigation via JS that toggles a `.active`
class, and a slide counter (`3 / 12`) in the corner. Keep code samples
in `<pre><code>` blocks copied verbatim from `docs/workshop_1.md` so
the two stay in sync.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Workshop 1 — Getting Started with Python</title>
<style>
  * { box-sizing: border-box; }
  body { margin: 0; font-family: system-ui, sans-serif; background: #1e1e2e; color: #eee; }
  .slide { display: none; min-height: 100vh; padding: 6vh 8vw; flex-direction: column; justify-content: center; }
  .slide.active { display: flex; }
  h1 { font-size: 2.5em; }
  h2 { font-size: 2em; color: #89b4fa; }
  pre { background: #11111b; padding: 1em; border-radius: 8px; overflow-x: auto; }
  table { border-collapse: collapse; margin-top: 1em; }
  th, td { border: 1px solid #444; padding: 0.5em 1em; text-align: left; }
  #counter { position: fixed; bottom: 1em; right: 1.5em; opacity: 0.6; font-size: 0.9em; }
</style>
</head>
<body>

<section class="slide active">
  <h1>Workshop 1</h1>
  <h2>Getting Started with Python</h2>
</section>

<section class="slide">
  <h2>How does a computer work?</h2>
  <p>CPU + memory + storage. The CPU repeats: <b>fetch</b> → <b>decode</b> → <b>execute</b>, millions of times per second.</p>
</section>

<section class="slide">
  <h2>What is programming?</h2>
  <p>Writing <b>source code</b> in a language humans can read, that a computer can translate into instructions it understands.</p>
</section>

<section class="slide">
  <h2>What is Python?</h2>
  <p>High-level, interpreted, general-purpose programming language.</p>
</section>

<section class="slide">
  <h2>Your first program</h2>
  <pre><code># This line prints a greeting
print("Hello, World!")</code></pre>
</section>

<section class="slide">
  <h2>The console</h2>
  <pre><code>python workshop_1/calc.py</code></pre>
</section>

<section class="slide">
  <h2>Variables</h2>
  <pre><code>age = 25
name = "Ada"</code></pre>
</section>

<section class="slide">
  <h2>Data types</h2>
  <table>
    <tr><th>Type</th><th>Meaning</th><th>Example</th></tr>
    <tr><td>int</td><td>whole number</td><td>42</td></tr>
    <tr><td>float</td><td>decimal number</td><td>3.14</td></tr>
    <tr><td>str</td><td>text</td><td>"hello"</td></tr>
    <tr><td>bool</td><td>true/false</td><td>True</td></tr>
  </table>
</section>

<section class="slide">
  <h2>Why data types matter</h2>
  <pre><code>age = 25
print("Age: " + age)
# TypeError: can only concatenate str (not "int") to str</code></pre>
</section>

<section class="slide">
  <h2>Type casting</h2>
  <pre><code>age = 25
print("Age: " + str(age))  # works</code></pre>
</section>

<section class="slide">
  <h2>Operators</h2>
  <table>
    <tr><th>Op</th><th>Meaning</th><th>Example</th><th>Result</th></tr>
    <tr><td>%</td><td>modulo</td><td>7 % 2</td><td>1</td></tr>
    <tr><td>**</td><td>exponent</td><td>2 ** 3</td><td>8</td></tr>
    <tr><td>==</td><td>equal</td><td>3 == 3</td><td>True</td></tr>
  </table>
</section>

<section class="slide">
  <h2>Next up</h2>
  <p>Run the examples in <code>workshop_1/</code>. Homework: <code>python-127-homework-1</code>.</p>
</section>

<div id="counter">1 / 12</div>

<script>
  const slides = document.querySelectorAll('.slide');
  const counter = document.getElementById('counter');
  let current = 0;

  function show(i) {
    slides[current].classList.remove('active');
    current = (i + slides.length) % slides.length;
    slides[current].classList.add('active');
    counter.textContent = `${current + 1} / ${slides.length}`;
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ') show(current + 1);
    if (e.key === 'ArrowLeft') show(current - 1);
  });
  document.addEventListener('click', () => show(current + 1));
</script>

</body>
</html>
```

- [ ] **Step 2: Open the file in a browser and click/arrow through all 12 slides**

Confirm the counter updates correctly, no slide is blank, and every
code/table matches the corresponding section of `docs/workshop_1.md`.

- [ ] **Step 3: Commit**

```bash
git add "presentations/Workshop 1.html"
git commit -m "Add workshop 1 slide deck"
```

---

### Task 5: Homework repo — README

**Files:**
- Create: `../python-127-homework-1/README.md`
- Create: `../python-127-homework-1/README_ka.md`

**Interfaces:**
- Consumes: nothing.
- Produces: links to `EXERCISES.md` and `SUBMITTING.md` (Tasks 6–7), which must exist at those exact paths in the same repo.

This task and Tasks 6–8 build a second local directory, sibling to the
`python-127` working directory, that will become `python-127-homework-1`
once pushed in Task 9. Initialize it as its own git repo in Step 1.

- [ ] **Step 1: Create and initialize the sibling directory**

```bash
mkdir -p ../python-127-homework-1
cd ../python-127-homework-1
git init
```

- [ ] **Step 2: Write `README.md`**

```markdown
# Homework 1

This homework covers Workshop 1: variables, data types, type casting,
and operators.

- [EXERCISES.md](EXERCISES.md) — what to do
- [SUBMITTING.md](SUBMITTING.md) — how to submit (Git/GitHub walkthrough
  for first-timers — read this even if you think you know Git)

Georgian versions: [README_ka.md](README_ka.md),
[EXERCISES_ka.md](EXERCISES_ka.md), [SUBMITTING_ka.md](SUBMITTING_ka.md).
```

- [ ] **Step 3: Write `README_ka.md`**

```markdown
# დავალება 1

ეს დავალება მოიცავს პირველ ვორქშოფს: ცვლადებს, მონაცემთა ტიპებს, ტიპების
გადაყვანას და ოპერატორებს.

- [EXERCISES_ka.md](EXERCISES_ka.md) — რა უნდა გააკეთოთ
- [SUBMITTING_ka.md](SUBMITTING_ka.md) — როგორ გავაგზავნოთ (Git/GitHub
  ინსტრუქცია დამწყებთათვის — წაიკითხეთ ეს ფაილი, თუნდაც გგონიათ რომ Git
  იცით)

ინგლისური ვერსიები: [README.md](README.md), [EXERCISES.md](EXERCISES.md),
[SUBMITTING.md](SUBMITTING.md).
```

- [ ] **Step 4: Commit**

```bash
git add README.md README_ka.md
git commit -m "Add homework 1 README"
```

---

### Task 6: Homework repo — exercises

**Files:**
- Create: `../python-127-homework-1/EXERCISES.md`
- Create: `../python-127-homework-1/EXERCISES_ka.md`

**Interfaces:**
- Consumes: the operator/type-casting content from `docs/workshop_1.md` (Task 2) — exercises must stay within that scope.
- Produces: the exercise list and expected outputs that `.github/pull_request_template.md` (Task 8) checklist items reference by name (`exercise_1.py` … `exercise_5.py`).

- [ ] **Step 1: Write reference solutions and verify their output**

Write each of these to a scratch file, run with `python`, and record the
*actual* printed output verbatim — don't hand-write the expected output
from memory.

```python
# exercise_1.py — About me
name = "Ada"
age = 25
city = "Tbilisi"
print(f"My name is {name}, I am {age} years old, and I live in {city}.")
```

```python
# exercise_2.py — fix the bug (starter code has a TypeError)
age = 25
print("I am " + age + " years old")  # BUG: fix this line
```
Fixed version:
```python
age = 25
print("I am " + str(age) + " years old")
```

```python
# exercise_3.py — rectangle area and perimeter
width = 4
height = 7
area = width * height
perimeter = 2 * (width + height)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
```

```python
# exercise_4.py — odd or even
number = 17
is_even = number % 2 == 0
print(f"{number} is even: {is_even}")
```

```python
# exercise_5.py — bonus: seconds in a day and a week
seconds_per_day = 24 * 60 * 60
seconds_per_week = seconds_per_day * 7
print(f"Seconds in a day: {seconds_per_day}")
print(f"Seconds in a week: {seconds_per_week}")
```

Run each with `python <scratch_file>.py`, confirm no traceback except
exercise_2's starter (which must raise `TypeError: can only concatenate
str (not "int") to str`), then delete the scratch files.

- [ ] **Step 2: Write `EXERCISES.md`**

```markdown
# Exercises

Create these files inside your own folder:
`submissions/<your-github-username>/`.

## exercise_1.py — About me

Print a sentence about yourself using an f-string with your name, age,
and city.

Example output:
```
My name is Ada, I am 25 years old, and I live in Tbilisi.
```

## exercise_2.py — Fix the bug

This code raises a `TypeError`. Copy it into `exercise_2.py`, then fix
it using type casting so it runs without error and prints
`I am 25 years old`.

```python
age = 25
print("I am " + age + " years old")  # BUG: fix this line
```

## exercise_3.py — Rectangle

Given `width = 4` and `height = 7`, print the area and perimeter.

Expected output:
```
Area: 28
Perimeter: 22
```

## exercise_4.py — Odd or even

Given `number = 17`, use `%` to determine if it's even, and print the
result as a `bool`.

Expected output:
```
17 is even: False
```

## exercise_5.py — Bonus: seconds in a day and a week

Print how many seconds are in a day and in a week, computed from
`60 * 60 * 24` (don't hardcode the final numbers).

Expected output:
```
Seconds in a day: 86400
Seconds in a week: 604800
```
```

- [ ] **Step 3: Write `EXERCISES_ka.md`** (Georgian translation, same structure)

```markdown
# სავარჯიშოები

შექმენით ეს ფაილები თქვენს საკუთარ საქაღალდეში:
`submissions/<თქვენი-github-username>/`.

## exercise_1.py — ჩემს შესახებ

დაბეჭდეთ წინადადება საკუთარ თავზე f-string-ის გამოყენებით: სახელი,
ასაკი და ქალაქი.

მაგალითი:
```
My name is Ada, I am 25 years old, and I live in Tbilisi.
```

## exercise_2.py — შეასწორეთ შეცდომა

ეს კოდი აგდებს `TypeError`-ს. დააკოპირეთ `exercise_2.py`-ში და
შეასწორეთ ტიპის გადაყვანის (casting) გამოყენებით, რომ იმუშაოს
შეცდომის გარეშე და დაბეჭდოს `I am 25 years old`.

```python
age = 25
print("I am " + age + " years old")  # ბაგი: გამოასწორეთ ეს ხაზი
```

## exercise_3.py — მართკუთხედი

`width = 4`-ისა და `height = 7`-ის გათვალისწინებით, დაბეჭდეთ ფართობი
და პერიმეტრი.

მოსალოდნელი შედეგი:
```
Area: 28
Perimeter: 22
```

## exercise_4.py — ლუწი თუ კენტი

`number = 17`-ის გათვალისწინებით, გამოიყენეთ `%` რომ დაადგინოთ არის თუ
არა ლუწი, და დაბეჭდეთ შედეგი როგორც `bool`.

მოსალოდნელი შედეგი:
```
17 is even: False
```

## exercise_5.py — ბონუსი: წამები დღეში და კვირაში

დაბეჭდეთ რამდენი წამია დღეში და კვირაში, გამოთვლილი
`60 * 60 * 24`-დან (არ ჩაწეროთ საბოლოო რიცხვები პირდაპირ).

მოსალოდნელი შედეგი:
```
Seconds in a day: 86400
Seconds in a week: 604800
```
```

- [ ] **Step 4: Commit**

```bash
git add EXERCISES.md EXERCISES_ka.md
git commit -m "Add homework 1 exercises"
```

---

### Task 7: Homework repo — submission walkthrough

**Files:**
- Create: `../python-127-homework-1/SUBMITTING.md`
- Create: `../python-127-homework-1/SUBMITTING_ka.md`
- Create: `../python-127-homework-1/submissions/README.md`
- Create: `../python-127-homework-1/submissions/README_ka.md`

**Interfaces:**
- Consumes: nothing.
- Produces: the branch-naming and PR-title conventions that `.github/pull_request_template.md` (Task 8) must match exactly (`"Homework 1 - Your Name"`, branch = GitHub username).

- [ ] **Step 1: Write `SUBMITTING.md`**

```markdown
# How to submit — with a Pull Request

You've never done this before, and that's fine — every step is here.
A **fork** is your own copy of this repository on GitHub. A **branch**
is where your changes live. A **Pull Request (PR)** asks to bring your
branch's changes into the original repository.

## 1. Install Git

- **Windows:** install [Git for Windows](https://git-scm.com/download/win). Use "Git Bash" (installed alongside it) as your terminal for the rest of these steps.
- **macOS:** open Terminal and run `git --version` — if it's not installed, macOS will prompt you to install it.
- **Linux:** `sudo apt install git` (Debian/Ubuntu) or your distro's package manager.

Confirm it worked:
```
git --version
```

## 2. Create a GitHub account

If you don't have one, sign up at [github.com](https://github.com).

## 3. Configure Git with your name and email

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 4. Fork this repository

Go to this repository's GitHub page and click **Fork** (top right).
Use the default settings. This creates
`https://github.com/<your-username>/python-127-homework-1`.

## 5. Clone YOUR fork

Replace `<your-username>` with your actual GitHub username:

```
git clone https://github.com/<your-username>/python-127-homework-1.git
cd python-127-homework-1
```

## 6. Create a branch named after your GitHub username

```
git checkout -b <your-username>
```

## 7. Create your folder and add your files

Inside `submissions/`, create a folder named after your GitHub
username, and put your exercise files there:

```
submissions/<your-username>/exercise_1.py
submissions/<your-username>/exercise_2.py
submissions/<your-username>/exercise_3.py
submissions/<your-username>/exercise_4.py
submissions/<your-username>/exercise_5.py
```

**Only your own folder.** Do not edit `README.md`, `EXERCISES.md`,
`SUBMITTING.md`, or any other student's folder.

## 8. Run every file before committing

```
python submissions/<your-username>/exercise_1.py
```

Compare the output to what `EXERCISES.md` says to expect.

## 9. Commit and push your branch

```
git add .
git commit -m "Add homework 1"
git push -u origin <your-username>
```

## 10. Open the Pull Request

GitHub will show a "Compare & pull request" banner on your fork's page
after pushing — click it. Or open one manually:

- **base repository:** `PythonADI/python-127-homework-1`, branch `main`
- **head repository:** `<your-username>/python-127-homework-1`, branch `<your-username>`

**Title:** `Homework 1 - Your Name` (your real name).

Fill in the checklist in the PR description template.

## 11. Wait for review

You cannot push directly to the original repository — its `main`
branch is protected. Your instructor is automatically requested as a
reviewer. If they ask for changes, push more commits to the **same
branch** — don't open a second PR. The PR updates automatically.
```

- [ ] **Step 2: Write `SUBMITTING_ka.md`** (Georgian translation, same 11 numbered sections and commands)

```markdown
# როგორ გავაგზავნოთ — Pull Request-ით

ეს არასდროს გაგიკეთებიათ და არაუშავს — ყველა ნაბიჯი აქ არის. **Fork**
არის ამ რეპოზიტორის თქვენი საკუთარი ასლი GitHub-ზე. **Branch** არის
ადგილი, სადაც თქვენი ცვლილებები ინახება. **Pull Request (PR)** სთხოვს
თქვენი branch-ის ცვლილებების შერწყმას ორიგინალ რეპოზიტორთან.

## 1. დააინსტალირეთ Git

- **Windows:** დააინსტალირეთ [Git for Windows](https://git-scm.com/download/win). გამოიყენეთ "Git Bash" ტერმინალად შემდეგი ნაბიჯებისთვის.
- **macOS:** გახსენით Terminal და გაუშვით `git --version`.
- **Linux:** `sudo apt install git` (Debian/Ubuntu).

დარწმუნდით რომ იმუშავა:
```
git --version
```

## 2. შექმენით GitHub ანგარიში

თუ არ გაქვთ, დარეგისტრირდით [github.com](https://github.com)-ზე.

## 3. დააკონფიგურირეთ Git თქვენი სახელით და ელფოსტით

```
git config --global user.name "თქვენი სახელი"
git config --global user.email "you@example.com"
```

## 4. Fork-ი გაუკეთეთ ამ რეპოზიტორს

გადადით ამ რეპოზიტორის GitHub გვერდზე და დააჭირეთ **Fork**-ს
(ზედა მარჯვენა კუთხეში).

## 5. Clone გაუკეთეთ თქვენს fork-ს

```
git clone https://github.com/<თქვენი-username>/python-127-homework-1.git
cd python-127-homework-1
```

## 6. შექმენით branch თქვენი GitHub username-ის სახელით

```
git checkout -b <თქვენი-username>
```

## 7. შექმენით თქვენი საქაღალდე და დაამატეთ ფაილები

`submissions/`-ის შიგნით შექმენით საქაღალდე თქვენი username-ით.

**მხოლოდ თქვენი საკუთარი საქაღალდე.** არ შეცვალოთ `README.md`,
`EXERCISES.md`, `SUBMITTING.md`, ან სხვა სტუდენტის საქაღალდე.

## 8. გაუშვით ყველა ფაილი commit-მდე

```
python submissions/<თქვენი-username>/exercise_1.py
```

## 9. Commit და push გაუკეთეთ თქვენს branch-ს

```
git add .
git commit -m "Add homework 1"
git push -u origin <თქვენი-username>
```

## 10. გახსენით Pull Request

**სათაური:** `Homework 1 - თქვენი სახელი`.

## 11. დაელოდეთ განხილვას

ვერ დააგზავნით პირდაპირ ორიგინალ რეპოზიტორში — მისი `main` branch
დაცულია. ინსტრუქტორი ავტომატურად ემატება როგორც reviewer.
```

- [ ] **Step 3: Write `submissions/README.md`**

```markdown
# Submissions

One folder per student, named after your GitHub username:

```
submissions/
  nino-b/
    exercise_1.py
    exercise_2.py
    ...
  giorgi-k/
    exercise_1.py
    exercise_2.py
    ...
```

Only touch your own folder. See [../SUBMITTING.md](../SUBMITTING.md)
for the full walkthrough.
```

- [ ] **Step 4: Write `submissions/README_ka.md`**

```markdown
# გამოგზავნები

თითო საქაღალდე თითო სტუდენტისთვის, დასახელებული თქვენი GitHub
username-ით:

```
submissions/
  nino-b/
    exercise_1.py
    ...
  giorgi-k/
    exercise_1.py
    ...
```

შეეხეთ მხოლოდ თქვენს საკუთარ საქაღალდეს. იხილეთ
[../SUBMITTING_ka.md](../SUBMITTING_ka.md) სრული ინსტრუქციისთვის.
```

- [ ] **Step 5: Commit**

```bash
git add SUBMITTING.md SUBMITTING_ka.md submissions/README.md submissions/README_ka.md
git commit -m "Add homework 1 submission walkthrough"
```

---

### Task 8: Homework repo — GitHub review machinery

**Files:**
- Create: `../python-127-homework-1/.github/CODEOWNERS`
- Create: `../python-127-homework-1/.github/pull_request_template.md`

**Interfaces:**
- Consumes: the PR title convention (`"Homework 1 - Your Name"`) and file list (`exercise_1.py` … `exercise_5.py`) from Tasks 6–7.
- Produces: nothing consumed by later tasks — this is the last local-content task before Task 9 pushes everything.

- [ ] **Step 1: Write `.github/CODEOWNERS`**

```
# Every file (*) is owned by the instructor, so GitHub automatically
# requests a review from @tavkhelidzeluka on every Pull Request.
* @tavkhelidzeluka
```

- [ ] **Step 2: Write `.github/pull_request_template.md`**

```markdown
## Homework 1 - Your Name

<!-- Replace "Your Name" above with your real name, fill in the two lines below, and tick every box that is true by changing [ ] to [x]. -->

**GitHub username:**

**Folder:** `submissions/<your-username>/`

### Checklist

* [ ] exercise_1.py … exercise_5.py are all present in my folder
* [ ] Every file runs with `python` without errors and prints the expected output from EXERCISES.md
* [ ] exercise_2.py no longer raises a TypeError
* [ ] I did not change any files outside my own folder
* [ ] My branch is named after my GitHub username

### Questions / notes for the reviewer

<!-- Anything you found hard, are not sure about, or want feedback on. It is fine to leave this empty. -->
```

- [ ] **Step 3: Commit**

```bash
git add .github/CODEOWNERS .github/pull_request_template.md
git commit -m "Add homework 1 CODEOWNERS and PR template"
```

---

### Task 9: Publish both repos and verify end-to-end

**Files:**
- None created — this task pushes the two local repos (`python-127`, `python-127-homework-1`) built in Tasks 1–8.

**Interfaces:**
- Consumes: every file created in Tasks 1–8.
- Produces: the live `PythonADI/python-127` and `PythonADI/python-127-homework-1` GitHub repos.

- [ ] **Step 1: Create the two GitHub repos**

Use the `github` MCP tool's repository-creation call (or `gh repo create`
if the CLI is available) to create:
- `PythonADI/python-127` (public, no auto-init — this repo already has commits locally)
- `PythonADI/python-127-homework-1` (public, no auto-init)

- [ ] **Step 2: Push `python-127`**

```bash
git remote add origin https://github.com/PythonADI/python-127.git
git branch -M main
git push -u origin main
```

- [ ] **Step 3: Push `python-127-homework-1`**

```bash
cd ../python-127-homework-1
git remote add origin https://github.com/PythonADI/python-127-homework-1.git
git branch -M main
git push -u origin main
```

- [ ] **Step 4: Verify CODEOWNERS and PR template render correctly**

On GitHub, open `PythonADI/python-127-homework-1` and confirm:
- Settings → the default branch is `main` and is where `.github/CODEOWNERS` lives (GitHub only honors CODEOWNERS on the default branch).
- Create a throwaway branch (e.g. `test-pr-flow`) directly on the repo (not a fork, since this is just verifying the mechanics), add a one-line change under a `submissions/_verify/` folder, push it, and open a PR back to `main`.
- Confirm the PR description is pre-filled with `pull_request_template.md`'s content, and that `@tavkhelidzeluka` is automatically added as a requested reviewer.
- Close the PR without merging, delete the `test-pr-flow` branch and the `submissions/_verify/` folder from `main` (via a follow-up commit) once confirmed.

- [ ] **Step 5: Verify `README.md` links resolve on GitHub**

Open `https://github.com/PythonADI/python-127` in a browser and click
every link in the workshop table (lesson doc, slides, homework repo) —
confirm none 404.

- [ ] **Step 6: Commit any cleanup from Step 4**

```bash
cd ../python-127-homework-1
git add .
git commit -m "Remove PR-flow verification artifacts"
git push
```
