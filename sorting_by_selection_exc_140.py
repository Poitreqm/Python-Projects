# Sorting by selection
# Implement array sorting by selection.

arr = [64, 25, 12, 22, 11, 1, 2, 4, 3, 8, 9, 128]

for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j

    tmp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = tmp


print(arr)
