# 2053. Kth Distinct String in an Array
# A distinct string is a string that is present only once in an array.
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".
# Note that the strings are considered in the order in which they appear in the array.


arr = ["d", "b", "c", "b", "c", "a"]
k = 2

ans = []

s = ""
for i in arr:
    tmp = arr.count(i)
    if tmp == 1:
        ans.append(i)
if len(ans) >= k:
    s = ans[k - 1]
else:
    s = ""

print(s)
