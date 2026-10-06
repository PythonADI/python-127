# The infinite loop: forget the change and the condition never turns False.
# The loop below is COMMENTED OUT on purpose - running it would never stop.
# If you ever start one by accident, press Ctrl+C to stop it.

# count = 1
# while count <= 3:
#     print(count)      # 1, forever - count never changes

# The fix is the missing change:
count = 1
while count <= 3:
    print(count)
    count += 1          # this is what the broken version forgot
