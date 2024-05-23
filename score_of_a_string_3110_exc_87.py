#
# 3110. Score of a String
# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
# Return the score of s.
#

s = "zaz"

count = 0
for i in range(len(s) - 1):
    count = count + abs(ord(s[i]) - ord(s[i + 1]))

print(count)
