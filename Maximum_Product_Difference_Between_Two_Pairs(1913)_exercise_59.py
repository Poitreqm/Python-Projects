#
# 1913. Maximum Product Difference Between Two Pairs
# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
# Return the maximum such product difference.
#

nums = [4, 2, 5, 9, 7, 4, 8]


temp_arr = []
result_array = []
variable = 0
indices = [(0, 1), (2, 3)]

for i in range(2):
    temp_arr.append(min(nums))
    nums.pop(nums.index(min(nums)))
    temp_arr.append(max(nums))
    nums.pop(nums.index(max(nums)))

temp_arr.sort()  # отсортировываем что бы две самые маленькие были в начале и две самые большие были в конце


for i, j in indices:
    result_array.append(temp_arr[i] * temp_arr[j])

variable = max(result_array) - min(result_array)

print(temp_arr)
print(result_array)
print(variable)
