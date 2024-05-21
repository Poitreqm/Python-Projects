#
# 1534. Count Good Triplets
# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.
#

arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3


count = 0

for i in range(0, len(arr) - 1):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if (
                abs(arr[i] - arr[j]) <= a
                and abs(arr[j] - arr[k]) <= b
                and abs(arr[i] - arr[k]) <= c
            ):
                count += 1


print(count)
