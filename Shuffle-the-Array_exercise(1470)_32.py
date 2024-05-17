#
# 1470. Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
#
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
#

nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4

x = 0
y = 0

count = 0
arr_x = nums[:n]  # срез - берем все элементы от 0 до n
arr_y = nums[n:]  # срез - берем все элементы от n до конца массива
new_arr = []

print(arr_x)
print(arr_y)

for i in nums:
    if x < y or x == y:
        new_arr.append(arr_x[x])
        x = x + 1
    else:
        new_arr.append(arr_y[y])
        y = y + 1

print(new_arr)
