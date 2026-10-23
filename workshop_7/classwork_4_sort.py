# Classwork: sorting, min, max, sum
#
# 1. summary(scores) returns three values: the lowest score, the highest
#    score and the average. Use min(), max(), sum() and len().
# 2. top(scores, count=3) returns a new list with the `count` highest
#    scores, biggest first. Use sorted(..., reverse=True) so the original
#    list is NOT changed.

def summary(scores):
    # TODO: return min, max and average, separated by commas
    pass

def top(scores, count=3):
    # TODO: sort a copy from high to low, then append the first `count`
    # items to a new list and return it
    pass

scores = [82, 95, 67, 90, 71]

low, high, average = summary(scores)
print(low, high, average)        # should print 67 95 81.0
print(top(scores))               # should print [95, 90, 82]
print(top(scores, count=1))      # should print [95]
print(scores)                    # should print [82, 95, 67, 90, 71]
