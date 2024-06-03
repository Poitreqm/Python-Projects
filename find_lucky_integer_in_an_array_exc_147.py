# 1394. Find Lucky Integer in an Array
# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
# Return the largest lucky integer in the array. If there is no lucky integer return -1.


arr = [2, 2, 2, 3, 3]
res = []


for i in range(len(arr)):
    if arr[i] == arr.count(arr[i]):
        res.append(arr[i])

    else:
        res.append(-1)

print(max(res))
