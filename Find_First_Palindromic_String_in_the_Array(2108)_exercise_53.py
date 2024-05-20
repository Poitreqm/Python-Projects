#
# 2108. Find First Palindromic String in the Array
# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.
#

words = ["def", "ghi"]

arr = []

for i in range(len(words)):
    if words[i] == words[i][::-1]:
        arr.append(words[i])


def firstPalindrome(words: list[str]) -> str:
    tmp = ""
    for i in range(len(words)):
        if words[i] == words[i][::-1]:
            tmp = words[i]
            return words[i]
            break
        else:
            tmp = ""
            


print(firstPalindrome(words))
