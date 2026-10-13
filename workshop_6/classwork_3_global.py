# Classwork: global vs. parameters
#
# use_herbs_global changes a global variable. Rewrite it as
# use_herbs(herbs, amount) that takes the current herbs and returns the
# new value, without using `global`.

herbs = 10

def use_herbs_global():
    global herbs
    herbs -= 1

use_herbs_global()
print(herbs)    # 9

def use_herbs(herbs, amount):
    # TODO: return herbs minus amount
    pass

herbs = use_herbs(herbs, 3)
print(herbs)    # should print 6
