# 1122. Relative Sort Array
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
# Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.


arr1 = [28, 6, 22, 8, 44, 17]
arr2 = [22, 28, 8, 6]

tmp_d = {}

not_found = []

res = []

for i in arr1:
    if i not in arr2:
        not_found.append(i)

for i in range(len(arr2)):
    tmp_d[arr2[i]] = arr1.count(arr2[i])

print(tmp_d)

for key, value in tmp_d.items():
    for _ in range(value):
        res.append(key)

not_found.sort()
res += not_found

print(res)
