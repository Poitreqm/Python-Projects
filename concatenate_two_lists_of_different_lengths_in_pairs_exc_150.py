# Concatenate two lists of different lengths in pairs
# Two lists are given: A and B. List A contains an integer number, and list B contains strings of arbitrary length.
# You need to write a pairs function that will return a list consisting of tuples with two elements: a number from list A and a string from list B.
# Note 1: The first element of list A is matched with the first element of list B, the second with the second, and so on.
# Note 2: If the length of any of the lists is longer, then the missing values must be filled with zeros.


A = [1, 2, 3]
B = ["aa", "vv"]

res = []

m = max(len(A), len(B))

for i in range(m):
    el_a = A[i] if i < len(A) else 0
    el_b = B[i] if i < len(B) else 0
    res.append((el_a, el_b))

print(res)
