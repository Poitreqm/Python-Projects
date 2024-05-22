#
# 1356. Sort Integers by The Number of 1 Bits
# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
# Return the array after sorting it.
#


arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]


arr.sort(key=lambda num: (num.bit_count(), num))

print(arr)
