#
# 1528. Shuffle String
# You are given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
#


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

arr = [0] * len(indices)
for i in range(len(s)):
    arr[indices[i]] = s[i]
print(arr)
