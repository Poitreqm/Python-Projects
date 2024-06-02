# Numbered tuples from the list of elements
# A list of arr with an arbitrary number of elements is given.
# You need to write a tuple_creator function that will return a list of tuples, each of which will contain an ordinal number and an arr list item.
# In this case, the numbering should not start from zero, but from some given number n.

arr = ["aaa", 125, "bbb"]
n = 3

a = []

for i in range(len(arr)):
    a.append((n + i, arr[i]))

print(a)
