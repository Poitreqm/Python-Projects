#
# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
#

nums = [0, 2, 1, 5, 3, 4]
arr = []


def buildArray(nums: list[int]) -> list[int]:
    for i in nums:
        arr.append(nums[i])
        # мы добавляем по индексу из-за этого на выходе будет [0, 1, 2, 4, 5, 3]
    return arr


print(buildArray(nums))
