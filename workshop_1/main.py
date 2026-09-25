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
