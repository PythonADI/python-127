# Workshop 12 — Growing the Portal: Templates, URLs and Models

## Prerequisites

- Workshop 11: you have the `workshop_11` project with three apps
  (`core`, `users`, `social`), a `Product` model, the admin, and a
  home page that lists products.
- Today we **keep building the same project**. We work in `workshop_11/`
  until Workshop 14.

## Project roadmap

| Workshop | Goal |
|----------|------|
| 11 | Project, apps, first model (`Product`), admin, list on home page ✅ |
| **12** | **Base template, named URLs, product detail page, search, blog posts** |
| 13 | Forms: create / edit / delete products and posts (CRUD) |
| 14 | Users: register, login, logout, only owners can edit; final polish |

## Today's tasks

Do the tasks **in order**. Run the server after every task and check
it in the browser:

```bash
uv run python manage.py runserver
```

---

### Task 1 — One base template for every page

**Problem:** every HTML file repeats `<html>`, `<head>` and the menu.
Change the menu once → you edit every file.

**Do:**

1. Create `templates/base.html` with the full page skeleton and a menu
   linking to Home, About, Blog, Friends, Login.
2. Put two blocks in it: `{% block title %}` and `{% block content %}`.
3. Rewrite `index.html`, `about.html` and `logout.html` to start with
   `{% extends "base.html" %}` and fill only the blocks.

<details>
<summary>Hint</summary>

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Portal{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Home</a> |
        <a href="/about/">About</a> |
        <a href="/blog/">Blog</a>
    </nav>
    {% block content %}{% endblock %}
</body>
</html>
```

```html
<!-- templates/about.html -->
{% extends "base.html" %}

{% block title %}About us{% endblock %}

{% block content %}
    <h1>About Us</h1>
{% endblock %}
```
</details>

✅ **Check:** every page shows the same menu, and you only wrote it once.

---

### Task 2 — Named URLs

**Problem:** `href="/about/"` breaks if we ever change the address.

**Do:**

1. Give every `path(...)` in `workshop_11/urls.py` a `name=`
   (`"home"`, `"about"`, `"blog"`, `"friends"`, `"login"`, `"logout"`).
2. In `base.html`, replace hard-coded links with `{% url 'home' %}` etc.

<details>
<summary>Hint</summary>

```python
path('about/', about_view, name="about"),
```

```html
<a href="{% url 'about' %}">About</a>
```
</details>

✅ **Check:** change `'about/'` to `'about-us/'` in `urls.py` — the menu
link still works without touching HTML.

---

### Task 3 — Product detail page

**Goal:** click a product on the home page → see its own page with all
fields.

**Do:**

1. In `core/views.py` add `product_detail_view(request, pk)`.
   Use `get_object_or_404(Product, pk=pk)`.
2. Add the URL `path('products/<int:pk>/', ..., name="product_detail")`.
3. Create `templates/product_detail.html` (extends `base.html`) showing
   name, price, description, production and expiry date.
4. In `index.html`, make every product name a link:
   `{% url 'product_detail' product.pk %}`.

<details>
<summary>Hint</summary>

```python
from django.shortcuts import render, get_object_or_404

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})
```
</details>

✅ **Check:** `/products/1/` shows the first product, `/products/999/`
shows a **404** page (not a crash).

**Talk about:** what is `pk`? Where does the number in the URL go?

---

### Task 4 — Search products

**Goal:** a search box on the home page filters products by name.

**Do:**

1. In `index.html` add a form with `method="get"` and an input
   `name="search"`.
2. In `home_view`, read `request.GET.get("search")`. If it is not
   empty, filter: `Product.objects.filter(name__icontains=search)`.
3. Keep the typed text in the input after searching
   (`value="{{ search }}"`).
4. Show `No products found.` when the list is empty
   (`{% empty %}` inside `{% for %}`).

<details>
<summary>Hint</summary>

```python
def home_view(request):
    search = request.GET.get("search", "")
    products = Product.objects.all()
    if search:
        products = products.filter(name__icontains=search)
    return render(request, "index.html", {"products": products, "search": search})
```
</details>

✅ **Check:** the URL becomes `/?search=milk` — notice where the data
went. Remove the `print(...)` lines from `home_view`.

---

### Task 5 — Order and clean up `Product`

**Do:**

1. Add `__str__` to `Product` so the admin shows the name instead of
   `Product object (1)`.
2. Add `class Meta: ordering = ["name"]`.
3. In `core/admin.py`, use a `ModelAdmin` with `list_display`
   (name, price, expiry_date) and `search_fields = ["name"]`.

✅ **Check:** the admin list has columns and a search box.

---

### Task 6 — Blog posts (the `social` app)

**Goal:** `/blog/` lists real posts from the database.

**Do:**

1. In `social/models.py` create `Post` with:
   `title` (CharField), `body` (TextField),
   `created_at` (`DateTimeField(auto_now_add=True)`).
   Add `__str__` and order newest first (`ordering = ["-created_at"]`).
2. Run `makemigrations` and `migrate`.
3. Register `Post` in `social/admin.py` and add 3 posts via the admin.
4. Change `blog_view` to render `templates/blog.html` with all posts.
5. **Bonus:** add a post detail page, exactly like Task 3.

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

✅ **Check:** `/blog/` shows posts, newest on top, inside the base layout.

---

## Homework

1. Finish any tasks you did not complete in class.
2. Add a `Category` model in `core` (just `name`) and a
   `category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)`
   field on `Product`. Show the category on the product detail page.
3. Home page: add links to filter by category
   (`/?category=3` → `products.filter(category_id=3)`).
4. Products whose `expiry_date` is in the past should show **(expired)**
   next to their name. Hint: pass `today` from the view, or add a
   method `is_expired()` on the model.

## Teacher notes

- Task 1–2 (~30 min): show the "change one link in 5 files" pain first,
  then fix it.
- Task 3 (~25 min): draw the flow URL → `pk` → view → DB → template.
- Task 4 (~20 min): open DevTools → Network to show GET query string.
- Task 5–6 (~35 min): Task 6 repeats Workshop 11 (model → migrate →
  admin → view → template) on their own; walk around and help.
- Do **not** introduce forms that save data (POST) yet — that is
  Workshop 13. `users` app stays untouched until Workshop 14.
