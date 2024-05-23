#
# 905. Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
#

nums = [3, 1, 2, 4]

arr_parity = []
arr_non_parity = []
for i in nums:
    if i % 2 == 0:
        arr_parity.append(i)
    else:
        arr_non_parity.append(i)


arr_parity.sort()
arr_non_parity.sort()

print(arr_parity + arr_non_parity)
