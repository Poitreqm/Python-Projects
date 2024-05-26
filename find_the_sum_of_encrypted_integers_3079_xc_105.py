# 3079. Find the Sum of Encrypted Integers
# You are given an integer array nums containing positive integers. We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.
# Return the sum of encrypted elements.

nums = [10, 21, 31]

sum = 0


for i in range(len(nums)):
    max_digit = max(str(nums[i]))
    tmp_str = ""
    for char in str(nums[i]):
        tmp_str = tmp_str + max_digit

    nums[i] = tmp_str


for i in nums:
    sum = sum + int(i)

print(sum)
