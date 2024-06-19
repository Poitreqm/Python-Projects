# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# WITHOUT SORT().

number = 15

arr = list(str(number))

print(arr)


for i in range(0, len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

print("".join(arr))
