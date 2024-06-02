# You are given 2 sets of numbers arr1 and arr2 as a Python list. It is necessary to return a list consisting of intersection elements. Duplicates must be deleted.
# Task
# Write a Pure Intersection function that will return a list with unique intersection elements.
# The PureIntersection function accepts input:
# arr1 is the first list with numbers
# arr2 is the second list with numbers
# Important: If the intersection is empty, then we return an empty list.

arr1 = [1, 2, 3]
arr2 = [1, 2, 15, 3, 3]


d = set()
res = []

for i in arr1:
    if i in arr2:
        d.add(i)

for i in d:
    res.append(i)

print(res)
