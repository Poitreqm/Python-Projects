# Sort the array by the frequency of occurrence of elements
# An array of integers is given. It is necessary to sort the array in ascending order of the frequency of occurrence of elements in the array.
# If several values occur in the array the same number of times, then it is necessary to arrange such elements in descending order of values.

arr = [1, 2, 2, 3, 4, 4]

d = set()

res = []


for i in arr:
    d.add((i, arr.count(i)))

sorted_d = sorted(d, key=lambda x: x[1])  # сортируем по второму числу


for i in sorted_d:

    tmp = i[1]
    if tmp == 1:
        res.append(i[0])
    elif tmp >= 2:
        for j in range(tmp):
            print(i[0])
            res.append(i[0])

print(res)
