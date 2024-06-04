# The product of all the members of the array
# Write a multiplier function that will return the product of all the members of the arr array.


nums = [1, 2, 3, 4, 5]

s = 1
for i in range(len(nums)):
    s *= nums[i]
print(s)
