# The sum of 2 numbers
# An array of integers nums and an integer target is given.
# Return the indexes of 2 numbers from the nums array, which add up to the target number.
# If the target can be obtained in several ways, then only one is returned as a result.


nums = [2, 7, 11, 15]
target = 9


for i in range(0, len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
