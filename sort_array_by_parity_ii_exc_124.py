# 922. Sort Array By Parity II
# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.


nums = [2, 3]

arr1 = []
arr2 = []
res = []
for i in nums:
    if i % 2 == 0:
        arr1.append(i)
    if i % 2 != 0:
        arr2.append(i)


m = max(len(arr1), len(arr2))

for i in range(m):
    res.append(arr1[i])
    res.append(arr2[i])

print(res)
