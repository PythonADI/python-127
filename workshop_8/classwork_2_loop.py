# Classwork: looping over a dictionary
#
# Write receipt(prices) that prints every item and its price, one per
# line as "item: price", and then returns the total.
# Use .items().

def receipt(prices):
    s = 0
    for item, price in prices.items():
        s += price
        print(f"{item}: {price}")
    
    return s
    

total = receipt({"bread": 2.5, "milk": 3.0, "cheese": 9.0})
print(f"Total: {total}")
# bread: 2.5
# milk: 3.0
# cheese: 9.0
# Total: 14.5
