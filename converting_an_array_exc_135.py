# Converting an array
# An array of integers nums of dimension 2n is given.
# The array elements are arranged in the following order: [x1,x2,...,xn,y1,y2,...,yn].
# It is necessary to convert the array to the form [x1,y1,x2,y2,...,xn,yn].


nums = [2, 5, 1, 3, 4, 7]
n = 3

res = []
for i in range(n):
    res.append(nums[:n][i])
    res.append(nums[n:][i])
print(res)
