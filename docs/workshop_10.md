# Workshop 10 — Virtual Environments and uv

## Prerequisites

- Workshop 9: you created a Django project with `uv init`, `uv add`
  and `uv run`. Today you find out **what those commands actually do**
  and **why** we use them.

## 1. The problem

Python can do a lot on its own. For more, you install **packages** —
code other people wrote, like Django. Packages have **versions**:
Django 4.2, Django 5.2, ...

Imagine your computer has **one** Python, and every package goes into
it:

```
Your computer
└── Python
    └── Django 5.2      ← everyone shares this one
```

Now you have two projects:

- `old_shop` was written two years ago and only works with **Django 4.2**
- `new_blog` is new and needs **Django 5.2**

There is room for only **one** Django. Install 4.2 and the blog
breaks. Install 5.2 and the shop breaks. 💥

## 2. The idea: one backpack per project

Give every project its **own backpack** of packages:

```
old_shop/
└── .venv/          ← old_shop's backpack
    └── Django 4.2

new_blog/
└── .venv/          ← new_blog's backpack
    └── Django 5.2
```

That backpack is called a **virtual environment** (venv for short).
It is a folder, usually called `.venv`, inside your project. It holds:

- its own copy of Python
- every package **this** project needs, and nothing else

The projects no longer see each other's packages, so they cannot break
each other.

A virtual environment is **just a folder**. Nothing magic. Delete it
and you can rebuild it in a few seconds.

## 3. uv: one tool that does it all

**uv** creates the backpack, puts packages in it, and runs your code
with it. Five commands cover almost everything:

| Command | What it does |
|---------|--------------|
| `uv init` | Start a new project here |
| `uv add django` | Put a package in the backpack |
| `uv remove django` | Take a package out |
| `uv run python main.py` | Run your code **with** the backpack |
| `uv sync` | Rebuild the backpack from the lists |

### `uv init` — start a project

```
uv init new_blog
cd new_blog
```

```
new_blog/
├── .gitignore
├── .python-version    ← which Python version to use
├── README.md
├── main.py
└── pyproject.toml     ← the project's settings and package list
```

There is no `.venv` yet. It appears the first time you need it.

### `uv add` — install a package

```
uv add django
```

```
Creating virtual environment at: .venv
 + asgiref==3.13.0
 + django==5.2.18
 + sqlparse==0.6.1
```

uv creates `.venv`, downloads Django (and the small packages Django
needs) **into it**, and writes it down in `pyproject.toml` and
`uv.lock`:

```toml
# pyproject.toml
dependencies = [
    "django>=5.2.18",
]
```

Need an older version? Say so:

```
uv add "django==4.2.*"
```

### `uv run` — run with the backpack

```
uv run python main.py
uv run python manage.py runserver
```

`uv run` means "use **this project's** backpack". You can see the
difference:

```
uv run python -c "import django; print(django.__version__)"
# 5.2.18

python -c "import django"
# ModuleNotFoundError: No module named 'django'
```

Plain `python` uses the **computer's** Python, where Django was never
installed. That is the most common beginner mistake — always use
`uv run`.

In the two projects from section 1, the same command prints a
different version in each folder:

```
cd old_shop
uv run python -c "import django; print(django.__version__)"
# 4.2.30

cd ../new_blog
uv run python -c "import django; print(django.__version__)"
# 5.2.18
```

## 4. The three things in your project

| File | Think of it as | Commit it to Git? |
|------|----------------|-------------------|
| `pyproject.toml` | The **shopping list**: "I need Django, at least 5.2" | ✅ Yes |
| `uv.lock` | The **receipt**: "I got exactly Django 5.2.18, and everything Django needs" | ✅ Yes |
| `.venv/` | The **shopping bag** with the actual stuff in it | ❌ Never |

Why never commit `.venv`?

- It is **big**: thousands of files.
- It only works on **your** computer. A `.venv` built on Windows does
  not work on a Mac.
- Anyone can rebuild it from the list and the receipt.

`uv init` already writes `.venv` into `.gitignore` for you.

## 5. Sharing a project

Your friend clones your project. They get `pyproject.toml` and
`uv.lock`, but no `.venv`. They run one command:

```
uv sync
```

uv reads the receipt (`uv.lock`) and builds a `.venv` with **exactly
the same versions** you have. Now the code runs the same on both
computers. No more "but it works on my machine!"

That is why, in Homework 9, you committed `pyproject.toml` and
`uv.lock`, but not `.venv`.

## 6. The old way: `venv` and `pip`

Before uv, people did the same job with tools built into Python. You
will see this in many tutorials, so it is good to recognise it:

```
python -m venv .venv               # 1. create the backpack

source .venv/Scripts/activate      # 2. put it on (Windows, Git Bash)
.venv\Scripts\activate             # 2. put it on (Windows, PowerShell)
source .venv/bin/activate          # 2. put it on (macOS / Linux)
# (.venv) appears at the start of your terminal line

pip install django                 # 3. put a package in it
pip freeze > requirements.txt      # 4. write down what is in it

deactivate                         # 5. take it off
```

"Activating" means "from now on, `python` in this terminal means the
backpack's Python". Forget to activate, and `pip install` puts Django
into the computer's Python again.

The same jobs with uv:

| Job | Old way | uv |
|-----|---------|----|
| Create the backpack | `python -m venv .venv` | happens automatically |
| Use it | activate, then `python ...` | `uv run python ...` |
| Install a package | `pip install django` | `uv add django` |
| Write down the list | `pip freeze > requirements.txt` | happens automatically |
| Rebuild on another computer | `pip install -r requirements.txt` | `uv sync` |

uv does the same jobs, but faster, and you cannot forget a step.

## 7. Common mistakes

| You see | Why | Fix |
|---------|-----|-----|
| `No module named 'django'` | You ran `python`, not `uv run python` | Start the command with `uv run` |
| ``error: No `pyproject.toml` found`` | You are not inside a project folder | `cd` into the project first |
| VS Code underlines `import django` in red | VS Code is looking at the computer's Python | **Ctrl + Shift + P** → "Python: Select Interpreter" → pick the one in `.venv` |
| Your Git commit has thousands of files | `.venv` got committed | Make sure `.gitignore` contains `.venv` |
| You deleted `.venv` by accident | Nothing is lost | `uv sync` |

## Quick reference

| Idea | Example |
|------|---------|
| Virtual environment | a `.venv` folder: this project's own Python and packages |
| New project | `uv init my_project` |
| Install a package | `uv add django` |
| Install an exact version | `uv add "django==4.2.*"` |
| Uninstall | `uv remove django` |
| Run code | `uv run python main.py` |
| Rebuild `.venv` | `uv sync` |
| Shopping list | `pyproject.toml` (commit) |
| Receipt | `uv.lock` (commit) |
| Shopping bag | `.venv/` (never commit) |

## What's next

Try it yourself: make two projects, give each a different Django
version, and check the version in each with `uv run`.
