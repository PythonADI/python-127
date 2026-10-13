# Classwork: input validation
#
# is_valid_password(password) returns True if the password has at least
# 8 characters AND contains at least one digit. ask_password() keeps
# asking until is_valid_password says yes, then returns the password.

def is_valid_password(password):
    # TODO: return False if shorter than 8; loop over the characters and
    # return True as soon as one is in "0123456789"; otherwise False
    pass

def ask_password():
    # TODO: while True: ask with input("Choose a password: "), return it
    # if valid, otherwise print "Too weak, try again."
    pass

print(is_valid_password("short1"))       # should print False
print(is_valid_password("longpassword")) # should print False
print(is_valid_password("longpass1"))    # should print True

ask_password()
print("Password accepted.")
