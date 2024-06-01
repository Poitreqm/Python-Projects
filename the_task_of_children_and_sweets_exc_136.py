# The task of children and sweets
# An array of integer candies is given, in the i place in which the number of candies of the i child is located. An integer number of extraCandies is also given.
# It is necessary to check for each child: if you give him extraCandies, will he have the most sweets?
# Note: There may be several children with the same amount of candy at the same time.

candies = [12, 1, 12]
extraCandies = 10

arr = []

for i in candies:
    if i + extraCandies >= max(candies):
        arr.append(True)
    else:
        arr.append(False)

print(arr)
