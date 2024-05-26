# 2206. Divide Array Into Equal Pairs
# You are given an integer array nums consisting of 2 * n integers.
# You need to divide nums into n pairs such that:
# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.


nums = [
    12,
    8,
    19,
    5,
    4,
    8,
    14,
    18,
    20,
    12,
    1,
    14,
    9,
    15,
    14,
    5,
    11,
    4,
    7,
    2,
    2,
    11,
    18,
    5,
    13,
    20,
    16,
    7,
    1,
    6,
    13,
    13,
    14,
    3,
    2,
    1,
    12,
    11,
    4,
    17,
    12,
    13,
    19,
    6,
    17,
    4,
    19,
    2,
    4,
    4,
    7,
    19,
    7,
    6,
    9,
    14,
    8,
    2,
    6,
    9,
    17,
    9,
    14,
    1,
    13,
    11,
    11,
    8,
    12,
    13,
    10,
    9,
    11,
    6,
    9,
    20,
    19,
    4,
    10,
    10,
    19,
    12,
    13,
    10,
    3,
    16,
    13,
    10,
    20,
    5,
    14,
    20,
    13,
    14,
    3,
    7,
    15,
    7,
    10,
    1,
]

arr = {}

count = 0
b = True
for i in nums:
    if i in arr:
        arr[i] += 1
    else:
        arr[i] = 1

for c in arr.values():
    if c % 2 != 0:
        b = False
        break

print(b)
