# 3069. Distribute Elements Into Two Arrays I
# You are given a 1-indexed array of distinct integers nums of length n.
# You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the ith operation:
# If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1. Otherwise, append nums[i] to arr2.
# The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].
# Return the array result.


nums = [5, 4, 3, 8]

result = []

arr1 = []
arr2 = []



for i in range(0, len(nums)):
    if i == 0:
        arr1.append(nums[0])
    elif i == 1:
        arr2.append(nums[1])
    else:
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])


result = arr1 + arr2

print(result)
