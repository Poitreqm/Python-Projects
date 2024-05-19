#
# 1313. Decompress Run-Length Encoded List
# We are given a list nums of integers representing a list compressed with run-length encoding.
# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
# Return the decompressed list.
#


nums = [1, 2, 3, 4]

arr = []

for i in range(len(nums) // 2):
    frequency = nums[2 * i]  # nums[2*i]
    value = nums[2 * i + 1]  #  nums[2*i+1]
    arr += [value] * frequency

print(arr)
