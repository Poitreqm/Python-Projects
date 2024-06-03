# Numbers with an even number of digits
# An array of integers is given. Find the number of numbers that have an even number of digits in the number entry.

nums = [12, 345, 2, 6, 7896]

count = 0
for i in range(len(nums)):
    tmp = len(str(nums[i]))
    if tmp % 2 == 0:
        count += 1

print(count)
