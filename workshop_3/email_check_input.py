# INTERACTIVE: a rough email sanity check using 'in' and 'not in' on a string.

MIN_LENGTH = 6

email = input("Email: ").strip().lower()

if "@" not in email:
    print("That's missing an @.")
elif "." not in email:
    print("A domain needs a dot, like example.com.")
elif len(email) < MIN_LENGTH:
    print("That looks too short to be real.")
else:
    print("Looks like an email address.")

# The same three checks as one condition, picking a value in one line.
looks_ok = "@" in email and "." in email and len(email) >= MIN_LENGTH
print(f"Verdict: {'ok' if looks_ok else 'needs fixing'}")
