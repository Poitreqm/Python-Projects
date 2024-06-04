# A combined list of different structures
# A list of integers A, tuple B, and set C is given. Implement the combine function, which will generate a list consisting of elements of all three data structures in the most elegant way.

A = [1, 2, 3]
B = (4, 5, 6)
C = {4, 5, 6}


arr = []

arr = [*A, *B, *C]

print(arr)
