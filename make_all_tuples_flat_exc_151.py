# Make all tuples flat
# The input is an arr array consisting of an arbitrary number of tuples, each of which also contains an arbitrary number of elements.
# You need to write a flat function that will return a list of all the elements that make up each tuple.


arr = [(1, 2, "a"), ("bb",), ("cc", "dd", 1)]

res = []

for i in range(len(arr)):
    res.extend(arr[i])


print(res)
