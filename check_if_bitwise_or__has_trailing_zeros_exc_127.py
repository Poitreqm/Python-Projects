# 2980. Check if Bitwise OR Has Trailing Zeros
# You are given an array of positive integers nums.
# You have to check if it is possible to select two or more elements in the array such that the bitwise OR of the selected elements has at least one trailing zero in its binary representation.
# For example, the binary representation of 5, which is "101", does not have any trailing zeros, whereas the binary representation of 4, which is "100", has two trailing zeros.
# Return true if it is possible to select two or more elements whose bitwise OR has trailing zeros, return false otherwise.


nums = [1, 3, 5, 7, 9]

count = 0
b = False
for i in nums:
    tmp = bin(i)
    if tmp[-1] == str(0):
        count += 1

if count >= 2:
    b = True

print(b)
