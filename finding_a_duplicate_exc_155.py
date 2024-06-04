# Finding a duplicate
# An array of numbers is given, which contains n+1 numbers in the interval [1, n].
# There is only one number in the nums array, which is repeated several times. Print this number

nums = [1, 2, 4, 3, 2]

r = 0
for i in nums:
    if nums.count(i) > 1:
        r = i
        break

print(r)
