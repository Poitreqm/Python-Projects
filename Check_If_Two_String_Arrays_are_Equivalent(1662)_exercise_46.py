#
# 1662. Check If Two String Arrays are Equivalent
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
#

word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]

if "".join(word1) == "".join(word2):
    print(True)
else:
    print(False)
