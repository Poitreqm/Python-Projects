# 1460. Make Two Arrays Equal by Reversing Subarrays
# You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.
# Return true if you can make arr equal to target or false otherwise.

target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]

target.sort()
arr.sort()

b = False

if target == arr:
    b = True
else:
    b = False

print(b)
