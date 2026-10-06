# python-127 — Workshop 4 Design (Loops)

## Context

Workshop 4 is the loops workshop. It follows the established pattern:

```
docs/workshop_4.md               — lesson text (English, workshop_3.md voice)
workshop_4/                      — one tiny .py file per concept
presentations/Workshop 4.html     — self-contained static deck
README.md                        — new table row for Workshop 4
```

Three agents build from this spec independently (doc, `.py` files, deck).
**Every code example in section 3 below is the single source of truth.**
Copy it character-for-character into all three places. Do not improve,
rename, reformat, or re-indent anything. Do not add examples that are not
in section 3.

### Hard constraints on content

Students have finished Workshops 1–3: variables, types, casting, f-strings,
`input()`, string methods, booleans/truthiness, `if`/`elif`/`else`,
`and`/`or`/`not`, `in`, chained comparisons, conditional expressions.

They have **not** seen lists, tuples, dicts, sets, functions (`def`),
imports, `enumerate`, `zip`, comprehensions, or `f"{x=}"`-style debugging
beyond what Workshop 2 used. Therefore:

- **No list literals, no indexing, no `len()` on anything but a string.**
- Iterate over `range(...)` and over **strings** only.
- No `def`, no `import`, no dicts, no comprehensions.
- No `input()` in the animated examples (the deck must be able to show a
  full deterministic trace). Only `while_vs_for.py` stays input-free too —
  **no example in Workshop 4 uses `input()`**, unlike Workshop 3.
- `else` on a loop (`for ... else`) is **explicitly out of scope**. Do not
  mention it, not even as a footnote.
- `while True:` + `break` is **out of scope** (it needs `input()` to be
  motivated). Every `while` here has a real condition.

Repo style reminders, taken from `workshop_3/`:

- Each `.py` file opens with a one-line `#` comment saying what it shows.
- Real printed output goes in trailing `# output` comments, aligned
  loosely, e.g. `print(status)      # adult`.
- 4-space indentation. No docstrings. No `if __name__ == "__main__"`.

### Verification status

Every snippet in section 3 was executed with `python` (CPython 3.13 on
Windows) and the output pasted from the real run. Where a snippet is an
infinite loop it was run with its output truncated, and that is noted.
**All output in this spec is real. Reproduce it exactly.** Note that all
output is deliberately ASCII — an em dash in `break_early.py` mangled on
the Windows console, so it uses a plain `-`. Keep it that way.

---

## 1. Learning outcomes

After Workshop 4 a student can:

1. Explain why a loop is better than copy-pasting the same statement.
2. Write a `while` loop and name its three parts: the **setup** before the
   loop, the **condition**, and the **update** inside the body.
3. Diagnose an infinite loop, state its cause (the condition's variable is
   never updated), and fix it.
4. Write a `for` loop over `range(n)` and predict the numbers it produces.
5. Use all three forms — `range(stop)`, `range(start, stop)`,
   `range(start, stop, step)` — and state that `stop` is **never** included.
6. Correct an off-by-one bug: know that counting 1 to 5 needs `range(1, 6)`.
7. Loop over the characters of a string with `for letter in word:`.
8. Build an accumulator: initialise a total before the loop, add to it
   inside the loop, use it after the loop.
9. Count the items matching a condition by putting an `if` inside a loop.
10. Use `break` to leave a loop early and `continue` to skip the rest of one
    pass, and say precisely which lines each one skips.
11. Write a nested loop and explain that the inner loop runs completely for
    every single pass of the outer loop.
12. Choose between `while` and `for`: `for` when the number of repeats is
    known up front, `while` when it depends on a changing condition.
13. Explain why reassigning the loop variable inside the body has no effect
    on the next pass.

---

## 2. Section outline for `docs/workshop_4.md`

13 numbered sections, mirroring `workshop_3.md`'s granularity. The doc opens
with a `## Prerequisites` list and closes with `## What's next`, exactly as
Workshop 3 does.

Front matter:

```markdown
# Workshop 4 — Loops

## Prerequisites

- Workshop 1: variables, data types, type casting, f-strings, operators
- Workshop 2: `input()`, string methods, booleans, truthiness
- Workshop 3: `if`/`elif`/`else`, `and`/`or`/`not`, `in`, chained comparisons
```

| # | Heading | Purpose (one line) |
|---|---------|--------------------|
| 1 | Doing something many times | Show five copy-pasted `print`s and establish that repetition deserves its own construct. |
| 2 | The `while` loop | Introduce `while <condition>:` as "keep running this block as long as this stays `True`". |
| 3 | The three parts of a `while` loop | Name setup / condition / update, and trace a countdown pass by pass. |
| 4 | The infinite loop | Show the same loop with the update deleted, explain why it never stops, and give the fix (`Ctrl+C` to escape). |
| 5 | `for` and `range()` | Introduce `for n in range(5):` as the loop that counts for you, and the loop variable. |
| 6 | The three forms of `range()` | Derive `range(stop)`, `range(start, stop)`, `range(start, stop, step)`, and hammer in that `stop` is excluded (off-by-one). |
| 7 | Looping over a string | `for letter in word:` — a `for` loop does not need `range()` at all. |
| 8 | Accumulating a total | The accumulator pattern: initialise before, add inside, read after. |
| 9 | Counting with a condition inside the loop | Put an `if` in the body to count only the passes that match. |
| 10 | `break` — leaving early | Abandon the whole loop the moment the answer is found. |
| 11 | `continue` — skipping one pass | Skip the rest of *this* body and go straight to the next pass. |
| 12 | Nested loops | A loop inside a loop; the inner loop finishes completely per outer pass. |
| 13 | `while` or `for`? | The decision rule, with the same job written both ways. |

Trap placement (do not give traps their own numbered sections):

- **Infinite loop** → section 4, which is entirely about it.
- **Mutating the loop variable** → short block at the end of section 5.
- **Off-by-one with `range`** → second half of section 6.

`## What's next` ends the doc:

```markdown
## What's next

See `workshop_4/` for runnable examples, and your homework in
[python-127-homework-4](https://github.com/PythonADI/python-127-homework-4).
```

---

## 3. Exact code examples (verified)

The literal source for every section. Output comments are real.

### §1 — `laps_by_hand.py`

```python
print("Lap 1")
print("Lap 2")
print("Lap 3")
print("Lap 4")
print("Lap 5")
```

Real output:

```
Lap 1
Lap 2
Lap 3
Lap 4
Lap 5
```

### §2 — `laps_while.py`

```python
lap = 1

while lap <= 5:
    print(f"Lap {lap}")
    lap = lap + 1

print("Done.")
```

Real output:

```
Lap 1
Lap 2
Lap 3
Lap 4
Lap 5
Done.
```

### §3 — `countdown.py`

```python
count = 3

while count > 0:
    print(count)
    count = count - 1

print("Liftoff!")
```

Real output:

```
3
2
1
Liftoff!
```

Verified pass-by-pass state (used by the animation; derived from the run):

| pass | condition checked | result | printed | `count` after update |
|------|-------------------|--------|---------|----------------------|
| 1 | `3 > 0` | `True` | `3` | `2` |
| 2 | `2 > 0` | `True` | `2` | `1` |
| 3 | `1 > 0` | `True` | `1` | `0` |
| 4 | `0 > 0` | `False` | — | loop exits |

### §4 — `infinite_loop.py`

```python
# DO NOT RUN THIS without being ready to press Ctrl+C.
# 'count' is never updated, so count > 0 stays True forever.
count = 3

while count > 0:
    print(count)
```

Real output (verified by running it and truncating; it never stops):

```
3
3
3
3
3
...
```

The fix, shown immediately after in the same file:

```python
# The fix: update the variable the condition depends on.
count = 3

while count > 0:
    print(count)
    count = count - 1
```

Real output of the fix:

```
3
2
1
```

### §5 — `range_basics.py`

```python
for n in range(5):
    print(n)
```

Real output:

```
0
1
2
3
4
```

### §5 trap — `loop_variable.py`

```python
# Changing the loop variable inside the body does not affect the next pass:
# 'range' hands 'n' a fresh value each time round.
for n in range(3):
    n = n * 10
    print(n)
```

Real output:

```
0
10
20
```

### §6 — `range_forms.py`

```python
for n in range(3):
    print(n)

print("---")

for n in range(2, 5):
    print(n)

print("---")

for n in range(0, 10, 3):
    print(n)
```

Real output:

```
0
1
2
---
2
3
4
---
0
3
6
9
```

The off-by-one half of §6, second snippet in the same file:

```python
# 'stop' is never included - this is 1, 2, 3, 4 and not 1 to 5.
for n in range(1, 5):
    print(n)
```

Real output:

```
1
2
3
4
```

(The doc states the fix in prose: to count 1 to 5, write `range(1, 6)` —
which is exactly what `laps_while.py`'s `for` rewrite in §13 does.)

### §7 — `letters.py`

```python
for letter in "Python":
    print(letter)
```

Real output:

```
P
y
t
h
o
n
```

### §8 — `running_total.py`

```python
total = 0

for n in range(1, 6):
    total = total + n
    print(f"n = {n}, total = {total}")

print(f"The sum is {total}")
```

Real output:

```
n = 1, total = 1
n = 2, total = 3
n = 3, total = 6
n = 4, total = 10
n = 5, total = 15
The sum is 15
```

### §9 — `count_letters.py`

```python
word = "banana"
count = 0

for letter in word:
    if letter == "a":
        count = count + 1
    print(f"{letter} -> count = {count}")

print(f"'a' appears {count} times")
```

Real output:

```
b -> count = 0
a -> count = 1
n -> count = 1
a -> count = 2
n -> count = 2
a -> count = 3
'a' appears 3 times
```

### §10 — `break_early.py`

```python
for n in range(1, 11):
    if n == 4:
        print("Found 4 - stopping.")
        break
    print(n)

print("After the loop.")
```

Real output:

```
1
2
3
Found 4 - stopping.
After the loop.
```

### §11 — `skip_evens.py`

```python
for n in range(1, 7):
    if n % 2 == 0:
        continue
    print(n)

print("Only the odd ones.")
```

Real output:

```
1
3
5
Only the odd ones.
```

### §12 — `times_table.py`

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} x {col} = {row * col}")
    print("---")
```

Real output:

```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
---
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
---
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
---
```

### §13 — `while_vs_for.py`

Snippet A (the number of repeats is known — use `for`):

```python
for lap in range(1, 6):
    print(f"Lap {lap}")
```

Real output:

```
Lap 1
Lap 2
Lap 3
Lap 4
Lap 5
```

Snippet B (the number of repeats is not known up front — use `while`):

```python
balance = 100

while balance > 10:
    balance = balance // 2
    print(f"balance = {balance}")

print("Too small to split.")
```

Real output:

```
balance = 50
balance = 25
balance = 12
balance = 6
Too small to split.
```

The doc's decision rule, verbatim:

> Use a `for` loop when you know up front how many times to repeat — a
> fixed count, or every character of a string. Use a `while` loop when the
> answer is "until something becomes true", and you can't say in advance how
> many passes that will take.

---

## 4. File manifest for `workshop_4/`

One tiny file per concept, lowercase and descriptive, in teaching order.
Each file is exactly the snippet(s) from section 3, plus a leading one-line
`#` comment and trailing `# output` comments in the `workshop_3/` style.
No file prints anything not shown in section 3.

| File | Section | Contains |
|------|---------|----------|
| `laps_by_hand.py` | §1 | The five copy-pasted `print` calls. Header comment: the problem loops solve. |
| `laps_while.py` | §2 | The `while lap <= 5` version of the same five laps. |
| `countdown.py` | §3 | The 3-2-1-Liftoff countdown; header comment labels setup / condition / update inline on those three lines. |
| `infinite_loop.py` | §4 | The broken loop **commented out** so the file is safe to run, followed by the working fix. The commented block keeps a `# DO NOT RUN` warning above it. This is the one file that deviates: the broken code is inside `#` comments, the fix is live. |
| `range_basics.py` | §5 | `for n in range(5)`. |
| `loop_variable.py` | §5 | The `n = n * 10` trap. |
| `range_forms.py` | §6 | The three `range` forms separated by `print("---")`, then the `range(1, 5)` off-by-one snippet. |
| `letters.py` | §7 | `for letter in "Python"`. |
| `running_total.py` | §8 | The 1..5 accumulator with its per-pass trace. |
| `count_letters.py` | §9 | Counting `"a"` in `"banana"` with a per-letter trace. |
| `break_early.py` | §10 | `break` at `n == 4`. |
| `skip_evens.py` | §11 | `continue` on even `n`. |
| `times_table.py` | §12 | The 3×3 nested loop. |
| `while_vs_for.py` | §13 | Snippet A then snippet B, separated by a blank line and a `#` comment naming which is which. |

14 files. Every one must run cleanly under `python workshop_4/<file>.py`
with Python 3.12+ and print exactly the output recorded in section 3
(`infinite_loop.py` prints only the fix's `3 2 1`, since the broken half is
commented out).

---

## 5. Animation storyboard

This is the headline feature of the workshop. Every code slide that shows
execution gets a **step-through animation** so students see Python moving
through the code rather than reading a static block.

### 5.0 Shared animation mechanics (build this once, reuse everywhere)

Add to the Workshop 3 CSS/JS skeleton, keeping its design language (CSS
custom properties, `--accent: #0071e3`, `--code-bg: #f5f5f7`, SF-stack
type, `.slide` / `.split`, the liquid dot indicator, `prefers-reduced-motion`).

**Markup contract.** An animated slide is a `.slide.split` whose
`.visual-col` holds a `<div class="anim" data-steps="N">` containing:

```html
<div class="anim" data-steps="13">
  <pre class="code"><code><span class="l" data-line="1">count = 3</span>
<span class="l" data-line="2"></span>
<span class="l" data-line="3">while count &gt; 0:</span>
...</code></pre>
  <div class="panels">
    <div class="vars"><!-- var chips --></div>
    <div class="out"><!-- output lines --></div>
  </div>
  <div class="diagram"><!-- SVG flow, tiles, grid, bar --></div>
</div>
```

**Step driver.** A global `step` per slide, `0`-based, stored on the element
as `data-step`. The slide's current step is applied by setting
`anim.dataset.step = k`; all reveal state is pure CSS from that attribute,
so steps are reversible and idempotent.

**Keys / clicks.** `ArrowRight` and `Space` advance the step; when the last
step is reached, the *next* press moves to the next slide. `ArrowLeft` steps
back; at step `0` it goes to the previous slide and lands it at its **last**
step (so going backwards looks continuous). Clicking the slide = `ArrowRight`.
This preserves Workshop 3's controls exactly.

**Reduced motion / print.** When `prefers-reduced-motion: reduce`, set the
slide to its final step on entry, show all output lines at once, and disable
every transition. No automatic timers anywhere in the deck except the
infinite-loop spin (5.2), which must also freeze under reduced motion and
instead show a static "repeats forever" caption.

**Four reusable visual primitives.** Every storyboard below is expressed in
these; implement them once.

1. **Line highlight.** The current line gets a rounded `--accent`-tinted
   background (`rgba(0,113,227,0.12)`) and a 3px left bar in `--accent`;
   all other lines drop to `opacity: 0.45`. Transition `0.25s ease`.
   Lines that are *skipped* (greyed by `continue`/`break`) get
   `opacity: 0.2` and `text-decoration: line-through` in `--text-secondary`.
2. **Variable panel (`.vars`).** One chip per variable: a rounded
   `--code-bg` box with the name in `--text-secondary` and the value in
   monospace `--text-primary`. A value change plays a 0.3s pop
   (`scale(1.12)` → `1`) and the chip border flashes `--accent`. Unset
   variables render as `—`. A condition being evaluated appears as a
   separate badge below the chips: `count > 0 → True` with `True` in
   `--accent`, `False` in `#d93025`.
3. **Output panel (`.out`).** A dark-on-light terminal-ish box in
   `--code-bg` with a small `output` label. New lines append one at a time,
   fading in and sliding up 6px over 0.25s. The panel never scrolls in the
   finite examples — size it for the longest trace on the slide.
4. **Diagram layer (`.diagram`).** Per-slide SVG: the loop-flow graph
   (5.1/5.2), the range tile row (5.3/5.4), the character strip (5.5), the
   total bar (5.6), the tile row with fade-out (5.7/5.8), or the grid
   (5.9). A **token** is a 14px `--accent` filled circle that animates
   along SVG paths via `offset-path` / `offset-distance`, 0.4s
   `cubic-bezier(0.4,0,0.2,1)`.

**The loop-flow graph** (used by 5.1 and 5.2) is a fixed SVG:

```
        ┌──────────────────────────┐
        │                          │  loop-back arrow
        ▼                          │
  ◇ condition ──True──▶ ▭ body ────┘
        │
      False
        │
        ▼
    ▭ after the loop
```

The diamond is the condition, the rectangle the body, the lower rectangle
the statement after the loop. Three arrows are individually addressable:
`#arrow-true`, `#arrow-back`, `#arrow-exit`. Inactive arrows sit at
`--divider`; the arrow the token is traversing turns `--accent` and
thickens from 2px to 3px.

---

### 5.1 `while` loop — the travelling token (§3, `countdown.py`)

Code shown (lines numbered as displayed; line 2 and 6 are blank):

```
1  count = 3
2
3  while count > 0:
4      print(count)
5      count = count - 1
6
7  print("Liftoff!")
```

13 steps. Diagram: the loop-flow graph; body rectangle labelled
`print(count); count = count - 1`; lower rectangle labelled `print("Liftoff!")`.

| Step | Line highlighted | Variable panel | New output | Extra visual |
|------|------------------|----------------|------------|--------------|
| 0 | none | `count —` | (empty) | Graph drawn in `--divider`; token parked at the top of the loop-back arrow's entry. |
| 1 | 1 | `count 3` (pop) | — | Token slides down into the condition diamond. |
| 2 | 3 | `count 3` | — | Diamond outlined `--accent`; badge `3 > 0 → True`. |
| 3 | 4 | `count 3` | `3` | `#arrow-true` lights up; token travels diamond → body. |
| 4 | 5 | `count 3 → 2` (pop) | — | Token stays in the body rectangle; a small `-1` label flashes next to the chip. |
| 5 | 3 | `count 2` | — | `#arrow-back` lights up; token travels body → up → diamond. Badge `2 > 0 → True`. |
| 6 | 4 | `count 2` | `2` | `#arrow-true` lights; token diamond → body. |
| 7 | 5 | `count 2 → 1` (pop) | — | Token in body; `-1` flash. |
| 8 | 3 | `count 1` | — | `#arrow-back` lights; token travels up. Badge `1 > 0 → True`. |
| 9 | 4 | `count 1` | `1` | Token diamond → body. |
| 10 | 5 | `count 1 → 0` (pop) | — | Token in body; `-1` flash. |
| 11 | 3 | `count 0` | — | `#arrow-back` lights; token travels up. Badge `0 > 0 → False` in red; `#arrow-back` then fades to `--divider` and dims to 30% — the pass that does not happen. |
| 12 | 7 | `count 0` | `Liftoff!` | `#arrow-exit` lights `--accent`; token travels diamond → lower rectangle and settles there. Caption fades in under the graph: **the loop ran 3 times, then the condition failed**. |

Final output panel contents, matching the verified run exactly:
`3`, `2`, `1`, `Liftoff!`.

---

### 5.2 Infinite loop — the same diagram, spinning (§4, `infinite_loop.py`)

Code shown:

```
1  count = 3
2
3  while count > 0:
4      print(count)
```

Same loop-flow graph, but the body rectangle is labelled `print(count)` only,
and a dashed ghost slot sits under it labelled `(nothing updates count)` in
`--text-secondary`. `#arrow-exit` is drawn dashed and struck-through from
step 0 with the label `never taken`.

8 steps.

| Step | Line highlighted | Variable panel | New output | Extra visual |
|------|------------------|----------------|------------|--------------|
| 0 | none | `count —` | (empty) | Graph in `--divider`; `#arrow-exit` dashed + struck + 25% opacity. |
| 1 | 1 | `count 3` (pop) | — | Token drops into the diamond. |
| 2 | 3 | `count 3` | — | Badge `3 > 0 → True`. |
| 3 | 4 | `count 3` | `3` | `#arrow-true` lights; token → body. |
| 4 | 3 | `count 3` (border flashes `#d93025`, **no** value change) | — | `#arrow-back` lights; token travels up. Annotation points at the chip: **count never changed**. |
| 5 | 3 | `count 3` | — | Badge `3 > 0 → True` again — identical to step 2. A faint "same check, same answer" ghost of step 2's badge sits behind it. |
| 6 | 4 | `count 3` | `3` | Token → body. Output now `3`, `3`. |
| 7 | 3 and 4 both pulsing | `count 3` | `3` × many | **Spin mode**: the token loops condition → body → back continuously at ~0.6s per lap, the two lines alternate their highlight in time with it, and the output panel streams `3` forever, scrolling with the newest line at the bottom. `#arrow-exit` stays dashed/struck. A banner in `#d93025` fades in over the output: **this never stops — press Ctrl+C**. Under reduced motion the token freezes mid-arrow and the banner reads **repeats forever** with a static `3 3 3 3 3 ...` output. |
| 8 | 5 (newly inserted) | `count 3 → 2` (pop) | — | **The fix.** Spin stops; the line `    count = count - 1` slides into the code block at line 5 with an `--accent` left bar, the ghost slot in the body rectangle fills in solid, the output panel clears, and `#arrow-exit` turns solid `--accent` with the strike-through removed. Caption: **now the condition can become False**. (Pressing again moves on to the next slide rather than re-running the fixed trace — 5.1 already showed that.) |

---

### 5.3 `range(n)` — tiles materialising, `stop` struck out (§5, `range_basics.py`)

Code shown:

```
1  for n in range(5):
2      print(n)
```

Diagram: a horizontal row of **number tiles** — 56px rounded `--code-bg`
squares with the number in monospace. Tiles `0 1 2 3 4` live inside a thin
`--divider` bracket labelled `range(5) produces`. One extra tile `5` sits
**outside** the bracket, to the right, at 35% opacity with a
`line-through` and the label `stop — never included` in `--text-secondary`.

8 steps.

| Step | Line highlighted | Variable panel | New output | Extra visual |
|------|------------------|----------------|------------|--------------|
| 0 | none | `n —` | (empty) | Bracket drawn empty. The struck `5` tile is already visible outside it — students should see the excluded value before they see the included ones. |
| 1 | 1 | `n —` | — | Tiles `0 1 2 3 4` materialise left to right, 60ms apart, each fading in and scaling `0.9 → 1`. The struck `5` tile gives a single shake. |
| 2 | 1 | `n 0` (pop) | — | Tile `0` lifts 4px and turns `--accent` with white text; a thin pointer labelled `n` sits under it. |
| 3 | 2 | `n 0` | `0` | Tile `0` stays active; a hairline arc runs from the tile to the new output line. |
| 4 | 1 → 2 (both flash in sequence) | `n 1` (pop) | `1` | Pointer slides to tile `1`; tile `0` drops back to `--code-bg` but keeps a faint `--accent` border (already done). |
| 5 | 1 → 2 | `n 2` (pop) | `2` | Pointer slides to tile `2`. |
| 6 | 1 → 2 | `n 3` (pop) | `3` | Pointer slides to tile `3`. |
| 7 | 1 | `n 4` | `4` | Pointer slides to tile `4`, then — on the same step — travels toward the struck `5` tile, is blocked by the bracket edge (a 0.2s bounce back), and the loop ends. Tile `5` flashes its strike-through. Caption: **`range(5)` gives 5 numbers, starting at 0, and 5 is not one of them**. |

Output panel ends as `0 1 2 3 4`, one per line — the verified run.

---

### 5.4 `range(start, stop)` and `range(start, stop, step)` — re-derived (§6, `range_forms.py`)

One slide, three tile rows revealed in turn, each with its own code line
highlighted. The code block shows all three loops (the `print("---")` lines
included, since the real output contains `---`).

Code shown:

```
1  for n in range(3):
2      print(n)
3
4  print("---")
5
6  for n in range(2, 5):
7      print(n)
8
9  print("---")
10
11 for n in range(0, 10, 3):
12     print(n)
```

11 steps. Three brackets stacked vertically, labelled `range(3)`,
`range(2, 5)`, `range(0, 10, 3)`. Each has its excluded `stop` tile struck
out to the right of its bracket.

| Step | Line highlighted | Variable panel | New output | Extra visual |
|------|------------------|----------------|------------|--------------|
| 0 | none | `n —` | (empty) | All three brackets drawn empty and dim; only row 1 at full opacity. |
| 1 | 1 | `n —` | — | Row 1: tiles `0 1 2` materialise; struck tile `3` appears outside with `stop`. |
| 2 | 1–2 | `n` runs `0 → 1 → 2` (three pops, 0.35s apart, in one step) | `0`, `1`, `2` | Pointer walks tiles `0 1 2`, then bounces off the bracket edge at the struck `3`. |
| 3 | 4 | `n 2` | `---` | Row 1 dims to 45%. |
| 4 | 6 | `n 2` | — | Row 2 comes to full opacity. A `start` pointer lands on tile `2`; tiles `2 3 4` materialise; struck tile `5` appears outside with `stop`. Annotation: **first number is `start`**. |
| 5 | 6–7 | `n` runs `2 → 3 → 4` | `2`, `3`, `4` | Pointer walks `2 3 4`, bounces at the struck `5`. |
| 6 | 9 | `n 4` | `---` | Row 2 dims to 45%. |
| 7 | 11 | `n 4` | — | Row 3 at full opacity. The full span `0 … 9` is sketched as 10 faint ghost tiles with the struck `10` outside; then only `0`, `3`, `6`, `9` solidify, joined by three `+3` hop arcs above them. Annotation: **third number is the `step` — the size of each hop**. |
| 8 | 11–12 | `n` runs `0 → 3 → 6 → 9` | `0`, `3`, `6`, `9` | Pointer hops along the arcs. |
| 9 | 11 | `n 9` | — | A fourth ghost hop arcs from `9` to `12`, which appears **past** the struck `10` tile, greyed, and immediately fades out. Caption: **the next hop would pass `stop`, so the loop ends**. |
| 10 | none | `n 9` | — | **Off-by-one payoff.** The code block cross-fades to the §6 trap snippet (`for n in range(1, 5):` / `print(n)`); a fresh row shows tiles `1 2 3 4` with struck `5`, output shows `1 2 3 4`, and a second row directly beneath re-derives `range(1, 6)` → tiles `1 2 3 4 5` with struck `6`. Caption, side by side: **`range(1, 5)` stops at 4. To count 1 to 5, write `range(1, 6)`.** |

All output shown matches the verified run:
`0 1 2 --- 2 3 4 --- 0 3 6 9` and `1 2 3 4`.

---

### 5.5 `for` over a string — each character in turn (§7, `letters.py`)

Code shown:

```
1  for letter in "Python":
2      print(letter)
```

Diagram: a **character strip** — six adjacent 56px boxes spelling
`P y t h o n`, framed as one word with a thin `--divider` outline and the
label `"Python"`. Below it a single chip labelled `letter`.

8 steps.

| Step | Line highlighted | Variable panel | New output | Extra visual |
|------|------------------|----------------|------------|--------------|
| 0 | none | `letter —` | (empty) | Strip drawn, all six boxes `--code-bg`. |
| 1 | 1 | `letter —` | — | Caption fades in: **no `range()` needed — a string is already a sequence of characters**. A pointer appears to the left of box `P`. |
| 2 | 1 → 2 | `letter "P"` (pop) | `P` | Box `P` turns `--accent` with white text and lifts 4px; the character visibly *copies* into the `letter` chip along a 0.3s arc; output gains `P`. |
| 3 | 1 → 2 | `letter "y"` (pop) | `y` | Box `P` returns to `--code-bg` with a faint accent border (visited); box `y` activates and copies into the chip. |
| 4 | 1 → 2 | `letter "t"` (pop) | `t` | Same, box `t`. |
| 5 | 1 → 2 | `letter "h"` (pop) | `h` | Same, box `h`. |
| 6 | 1 → 2 | `letter "o"` (pop) | `o` | Same, box `o`. |
| 7 | 1 | `letter "n"` | `n` | Same, box `n`; then the pointer runs off the right edge of the strip and the whole strip gets a completed accent outline. Caption: **six characters, six passes**. |

Output panel ends as `P y t h o n`, one per line — the verified run.

---

### 5.6 Accumulator — the growing total (§8, `running_total.py`)

Code shown:

```
1  total = 0
2
3  for n in range(1, 6):
4      total = total + n
5      print(f"n = {n}, total = {total}")
6
7  print(f"The sum is {total}")
```

Diagram: a tile row `1 2 3 4 5` (struck `6` outside the bracket, label
`range(1, 6)`), a large **`total` box** (120×80, `--code-bg`, monospace
value), and under it a horizontal **bar** whose width is
`total / 15` of the track. The track is labelled `0` at the left and `15`
at the right. Bar fill `--accent`, width transition `0.4s ease`.

8 steps. Bar widths are exact fractions of the verified totals.

| Step | Line highlighted | Variable panel | New output | Extra visual |
|------|------------------|----------------|------------|--------------|
| 0 | none | `total —`, `n —` | (empty) | Tile row and empty bar track drawn; `total` box shows `—`. |
| 1 | 1 | `total 0` (pop) | — | `total` box fills in `0`; bar at 0% width. Caption: **start the total before the loop**. |
| 2 | 3 | `total 0`, `n 1` (pop) | — | Tile `1` activates; a `+1` chip detaches from the tile and floats toward the `total` box. |
| 3 | 4–5 | `total 0 → 1` (pop), `n 1` | `n = 1, total = 1` | `+1` chip lands; `total` box shows `1`; bar grows to **6.7%** (1/15). |
| 4 | 3–5 | `total 1 → 3`, `n 2` | `n = 2, total = 3` | Tile `2` activates; `+2` chip flies in; bar grows to **20%** (3/15). |
| 5 | 3–5 | `total 3 → 6`, `n 3` | `n = 3, total = 6` | Tile `3`; `+3` chip; bar **40%** (6/15). |
| 6 | 3–5 | `total 6 → 10`, `n 4` | `n = 4, total = 10` | Tile `4`; `+4` chip; bar **66.7%** (10/15). |
| 7 | 3–5 | `total 10 → 15`, `n 5` | `n = 5, total = 15` | Tile `5`; `+5` chip; bar **100%**, and the bar flashes once. The pointer bounces off the struck `6` tile. |
| 8 | 7 | `total 15` | `The sum is 15` | Tile row dims to 35%; the `total` box scales to `1.08` and holds, outlined `--accent`. Caption: **the total outlives the loop — that's why it was created before it**. |

Output panel ends with the six verified lines.

---

### 5.7 `break` — leaving immediately (§10, `break_early.py`)

Code shown:

```
1  for n in range(1, 11):
2      if n == 4:
3          print("Found 4 - stopping.")
4          break
5      print(n)
6
7  print("After the loop.")
```

Diagram: a tile row `1 2 3 4 5 6 7 8 9 10` with the struck `11` outside the
bracket, label `range(1, 11)`. To the right of the loop block, a bold
**exit arrow** (`#arrow-break`) drawn dashed/dim from step 0, pointing from
line 4 straight down past line 5 to line 7.

9 steps.

| Step | Line highlighted | Variable panel | New output | Extra visual |
|------|------------------|----------------|------------|--------------|
| 0 | none | `n —` | (empty) | Tile row materialised; exit arrow dim. |
| 1 | 1 → 2 | `n 1` (pop) | — | Tile `1` activates; badge `1 == 4 → False` (red `False`); line 3–4 grey to 20% for this pass. |
| 2 | 5 | `n 1` | `1` | Token skips over lines 3–4 (a small hop arc on the left gutter) and lands on line 5. |
| 3 | 1 → 2 | `n 2` (pop) | — | Tile `2`; badge `2 == 4 → False`. |
| 4 | 5 | `n 2` | `2` | Same hop; output `2`. |
| 5 | 1 → 2 | `n 3` (pop) | — | Tile `3`; badge `3 == 4 → False`. |
| 6 | 5 | `n 3` | `3` | Output `3`. Tiles `1 2 3` now carry a visited accent border. |
| 7 | 1 → 2 → 3 | `n 4` (pop) | `Found 4 - stopping.` | Tile `4` activates and turns **`#d93025`**; badge `4 == 4 → True` with `True` in `--accent`; lines 3–4 come to full opacity for the first time. |
| 8 | 4, then 7 | `n 4` | `After the loop.` | `break` on line 4 pulses; `#arrow-break` turns solid `--accent` and the token shoots along it, skipping line 5 entirely — **line 5 greys with a strike-through**. Simultaneously tiles `5 6 7 8 9 10` fade from 100% to 15% with a single strike-through line drawn across them, 50ms apart left to right. Caption: **`break` abandons the whole loop — the remaining six numbers never happen**. |

Output panel ends as the verified
`1`, `2`, `3`, `Found 4 - stopping.`, `After the loop.`
Note there is **no** `4` in the output: `print(n)` is the line `break` skips.
The storyboard must make that the punchline.

---

### 5.8 `continue` — skipping the rest of one pass (§11, `skip_evens.py`)

Code shown:

```
1  for n in range(1, 7):
2      if n % 2 == 0:
3          continue
4      print(n)
5
6  print("Only the odd ones.")
```

Diagram: tile row `1 2 3 4 5 6`, struck `7` outside, label `range(1, 7)`.
A **short-circuit arc** (`#arrow-continue`) drawn dashed/dim from line 3
curving leftward and **up** to line 1 — the visual opposite of 5.7's
downward-and-out arrow. Students must see `break` goes *out and down*,
`continue` goes *back and up*.

8 steps.

| Step | Line highlighted | Variable panel | New output | Extra visual |
|------|------------------|----------------|------------|--------------|
| 0 | none | `n —` | (empty) | Tile row drawn; both the continue arc and line 4 at normal state. |
| 1 | 1 → 2 | `n 1` (pop) | — | Tile `1` activates; badge `1 % 2 == 0 → False`; line 3 greys for this pass. |
| 2 | 4 | `n 1` | `1` | Token hops over line 3 to line 4. |
| 3 | 1 → 2 → 3 | `n 2` (pop) | — | Tile `2` activates in `--text-secondary` (a skipped value); badge `2 % 2 == 0 → True`; line 3 `continue` pulses; **line 4 greys to 20% with a strike-through** — the skipped rest of the body. |
| 4 | 1 | `n 2` | — (nothing) | `#arrow-continue` turns solid `--accent`; the token leaves mid-body and arcs **back up** to line 1. Tile `2` settles at 25% opacity, struck. Output panel deliberately gains **no** line — annotate the panel with a faint `(nothing printed)` ghost that fades after 0.6s. Caption: **`continue` skips the rest of this pass, not the loop**. |
| 5 | 1 → 2 → 4 | `n 3` (pop) | `3` | Line 4 returns to full opacity (it was never deleted, just skipped once); tile `3` active; output `3`. |
| 6 | 1 → 2 → 3 → 1 | `n 4` (pop) | — | Tile `4` struck and dimmed; `continue` fires again; line 4 greys and the token arcs back up. |
| 7 | 1 → 2 → 4, then 1 → 2 → 3 → 1, then 6 | `n 5`, then `n 6` | `5`, then `Only the odd ones.` | `n = 5` prints (tile `5` active, output `5`); `n = 6` is skipped (tile `6` struck); the pointer then bounces off the struck `7` tile, `#arrow-continue` fades to dim, and the token drops to line 6. Final tile row reads: `1` `3` `5` accented, `2` `4` `6` struck — the whole lesson in one picture. |

Output panel ends as the verified `1`, `3`, `5`, `Only the odd ones.`

---

### 5.9 Nested loops — the filling grid (§12, `times_table.py`)

Code shown:

```
1  for row in range(1, 4):
2      for col in range(1, 4):
3          print(f"{row} x {col} = {row * col}")
4      print("---")
```

Diagram: a 3×3 **grid** of 72px cells, `--divider` borders, column headers
`col 1 2 3` and row headers `row 1 2 3`. Each cell is empty at step 0 and
fills with its product. A `row` chip and a `col` chip sit beside the grid.

13 steps. The output panel holds 12 lines (nine products plus three `---`),
so size it for 12.

| Step | Line highlighted | Variable panel | New output | Extra visual |
|------|------------------|----------------|------------|--------------|
| 0 | none | `row —`, `col —` | (empty) | Empty grid with headers. |
| 1 | 1 | `row 1` (pop) | — | Grid **row 1** gets a soft `--accent` tinted band across all three of its cells; its row header turns `--accent`. Caption: **the outer loop picks a row**. |
| 2 | 2 | `row 1`, `col 1` (pop) | — | Column header `1` turns `--accent`; cell (1,1) outlined. |
| 3 | 3 | `row 1`, `col 1` | `1 x 1 = 1` | Cell (1,1) fills: background `--accent` at 14%, value `1` scales in `0.8 → 1`. |
| 4 | 2 → 3 | `row 1`, `col 2` (pop) | `1 x 2 = 2` | Cell (1,2) fills `2`. |
| 5 | 2 → 3 | `row 1`, `col 3` (pop) | `1 x 3 = 3` | Cell (1,3) fills `3`. The `col` pointer then bounces off a struck `4` marker to the right of the grid (`range(1, 4)` excludes 4) — the inner loop is done. |
| 6 | 4 | `row 1`, `col 3` | `---` | Grid row 1 gets a completed solid `--accent` underline; the band fades. Caption: **the inner loop finished completely — now one outer pass is over**. |
| 7 | 1 | `row 2` (pop), `col 3` | — | Band and header highlight move down to grid row 2. Note the `col` chip still reads `3` — it has not been reset yet. |
| 8 | 2 | `row 2`, `col 1` (pop) | — | `col` resets to `1`; a small loop-arrow icon flashes beside the chip. Caption: **`range` starts the inner loop over from 1 every time**. |
| 9 | 3 → 2 → 3 → 2 → 3 | `row 2`, `col` runs `1 → 2 → 3` | `2 x 1 = 2`, `2 x 2 = 4`, `2 x 3 = 6` | Cells (2,1) (2,2) (2,3) fill `2`, `4`, `6` left to right, 0.3s apart. |
| 10 | 4 | `row 2`, `col 3` | `---` | Grid row 2 underlined complete. |
| 11 | 1 → 2 → 3 (repeating) | `row 3`, `col` runs `1 → 2 → 3` | `3 x 1 = 3`, `3 x 2 = 6`, `3 x 3 = 9` | Band moves to grid row 3; cells fill `3`, `6`, `9`. |
| 12 | 4, then none | `row 3`, `col 3` | `---` | Grid row 3 underlined; the `row` pointer bounces off its own struck `4` marker. Whole grid pulses once as a completed 3×3 block. Caption: **3 outer passes × 3 inner passes = 9 lines**. |

Output panel ends with the twelve verified lines, in order:
`1 x 1 = 1`, `1 x 2 = 2`, `1 x 3 = 3`, `---`,
`2 x 1 = 2`, `2 x 2 = 4`, `2 x 3 = 6`, `---`,
`3 x 1 = 3`, `3 x 2 = 6`, `3 x 3 = 9`, `---`.

---

### 5.10 Smaller animations (same primitives, fewer steps)

**§2 `laps_while.py`** — 7 steps, variable panel + output only, no diagram.
Highlight line 1 (`lap 1`), then for each of the five passes highlight
line 3 (badge `lap <= 5 → True`), line 4 (output `Lap N`), line 5
(`lap N → N+1`) **collapsed into one step per pass**, then a final step
with badge `6 <= 5 → False` and output `Done.` This is the warm-up; 5.1
is the full-fat version.

**§3 "three parts"** — static, not animated: the same `countdown.py` code with
three labelled brackets pointing at line 1 (**setup**), line 3
(**condition**), line 5 (**update**). It earns its own slide *before* 5.1 so
students have the vocabulary the token animation then uses.

**§5 trap `loop_variable.py`** — 4 steps. Per pass: highlight line 2, show
`n 0 → 0`, `n 1 → 10`, `n 2 → 20` with the chip visibly reset back to the
`range` value at the start of the next step, and a small ghost of the
previous pass's mutated value fading out above the chip. Caption on the last
step: **the next pass overwrites `n` — your change is thrown away**.

**§9 `count_letters.py`** — 8 steps, reusing 5.5's character strip plus a
`count` chip. Per letter: highlight line 4 (box activates, `letter` chip
updates), highlight line 5 with badge `letter == "a" → True/False`, and on
`True` highlight line 6 and pop `count`. Output per step, from the verified
run: `b -> count = 0`, `a -> count = 1`, `n -> count = 1`,
`a -> count = 2`, `n -> count = 2`, `a -> count = 3`, then
`'a' appears 3 times`. The three `a` boxes end accented, the `b`/`n` boxes
plain — the picture of "3".

**§13 `while_vs_for.py`** — two side-by-side static code panels with their
real output beneath each, plus the decision rule. Not animated: by this
point the mechanics are known and the slide is about choosing.

---

## 6. Deck slide list for `presentations/Workshop 4.html`

20 slides. Reuse the Workshop 3 skeleton verbatim (CSS variables, `.slide`,
`.slide.split`, `.content-col` / `.visual-col`, `pre`/`code`, `#dots` +
`#liquid`, the keyboard/click handler) and extend it with the 5.0 animation
layer. Every `.content-col` carries an `<h2>` plus one `p.body` of at most
two sentences — Workshop 3's density, not more.

| # | Slide | Type | Content |
|---|-------|------|---------|
| 1 | Title | static | `.title-slide`, eyebrow `Workshop 4`, `<h1>Loops</h1>`. |
| 2 | Doing something many times | static | §1 `laps_by_hand.py` in a `pre`. Body: five lines to say the same thing five times — and 500 would be 500 lines. |
| 3 | The `while` loop | **animated** (5.10 warm-up, 7 steps) | §2 `laps_while.py`. Body: keep running this block as long as the condition stays `True`. |
| 4 | The three parts | static | §3 `countdown.py` with the setup / condition / update brackets. Body: every `while` loop needs all three. |
| 5 | Watch it run | **animated** (5.1, 13 steps) | `countdown.py` with the loop-flow graph, travelling token, variable panel, output panel. The centrepiece. |
| 6 | The infinite loop | **animated** (5.2, 8 steps) | §4 `infinite_loop.py`. Body: delete the update and the condition can never become `False`. |
| 7 | `for` and `range()` | **animated** (5.3, 8 steps) | §5 `range_basics.py` with the tile row and the struck `5`. Body: `for` counts for you. |
| 8 | `stop` is never included | static | A single large graphic: the `range(5)` bracket holding `0 1 2 3 4` beside the struck `5`. Body: `range(5)` gives five numbers and starts at 0. (A still, memorisable version of slide 7's payoff.) |
| 9 | The loop variable is not yours to keep | **animated** (5.10, 4 steps) | §5 trap `loop_variable.py`. |
| 10 | The three forms of `range()` | **animated** (5.4, 11 steps) | §6 `range_forms.py`, three tile rows re-derived, ending on the off-by-one comparison. |
| 11 | Off-by-one | static | `range(1, 5)` → `1 2 3 4` above `range(1, 6)` → `1 2 3 4 5`, both with their struck `stop`. Body: to count 1 to 5, stop at 6. |
| 12 | Looping over a string | **animated** (5.5, 8 steps) | §7 `letters.py` with the character strip. Body: a `for` loop doesn't need `range()`. |
| 13 | Accumulating a total | **animated** (5.6, 9 steps) | §8 `running_total.py` with the `total` box and growing bar. Body: create it before, add inside, read after. |
| 14 | Counting with a condition | **animated** (5.10, 8 steps) | §9 `count_letters.py`, character strip plus `count` chip. Body: an `if` inside a loop counts only the passes that match. |
| 15 | `break` | **animated** (5.7, 9 steps) | §10 `break_early.py`. Body: leave the whole loop the moment you have your answer. |
| 16 | `continue` | **animated** (5.8, 8 steps) | §11 `skip_evens.py`. Body: skip the rest of this pass, then carry on. |
| 17 | `break` vs `continue` | static | Side-by-side diagram only (no new code): the downward-and-out arrow labelled `break — leaves the loop` next to the back-and-up arc labelled `continue — leaves this pass`. |
| 18 | Nested loops | **animated** (5.9, 13 steps) | §12 `times_table.py` with the filling 3×3 grid. Body: the inner loop finishes completely for every single outer pass. |
| 19 | `while` or `for`? | static | §13 `while_vs_for.py`, both snippets side by side with their real output, plus the decision rule from section 3. |
| 20 | Closing | static | `.title-slide` styling, `<h1>` reading `Loops`, with the four take-aways as a short list: `for` when you know the count, `while` when you don't, always update the condition's variable, `stop` is excluded. Footer line: `workshop_4/` and the homework repo link. |

Nine animated slides, eleven static. Static slides 8, 11 and 17 exist on
purpose — each is the still, screenshot-able distillation of the animation
just before it, for students re-reading the deck later.

---

## 7. README row

Append to the workshop table in `README.md`, matching the existing rows:

```markdown
| 4 | [Workshop 4](docs/workshop_4.md) | [Slides](presentations/Workshop%204.html) | [python-127-homework-4](https://github.com/PythonADI/python-127-homework-4) |
```

---

## 8. Out of scope

- `for ... else` / `while ... else` — deliberately skipped.
- `while True:` with `break`, and `input()`-driven loops.
- Lists, indexing, `enumerate`, `zip`, `sum`, comprehensions, `range` with a
  negative step.
- The `python-127-homework-4` repo contents (the README row links it; the
  repo itself follows the Workshop 1 pattern and needs no spec).

## 9. Verification before any of this ships

1. `python workshop_4/<file>.py` for all 14 files; output must match
   section 3 character for character.
2. Every code block in `docs/workshop_4.md` and every `<pre><code>` in
   `presentations/Workshop 4.html` diffed against section 3. Identical, or
   it is a bug.
3. Open the deck and step through all 20 slides with `ArrowRight` only,
   confirming every animated slide's final output panel equals the real
   program output, that `ArrowLeft` walks back through steps cleanly, and
   that `prefers-reduced-motion: reduce` shows every slide complete and
   still.
