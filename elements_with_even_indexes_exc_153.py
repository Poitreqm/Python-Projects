# Elements with even indexes
# The input is an array of integers arr. Write an even function that returns a list of values from the original arr list that have even indexes (indexing is counted from one).


arr = [1, 2, 3, 4, 4, 4]

res = []

for i in range(1, len(arr)):
    if i % 2 != 0:
        res.append(arr[i])

print(res)
