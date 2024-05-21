#
# 2744. Find Maximum Number of String Pairs
# You are given a 0-indexed array words consisting of distinct strings.
# The string words[i] can be paired with the string words[j] if:
# The string words[i] is equal to the reversed string of words[j].
# 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.
# Note that each string can belong in at most one pair.
#

word = ["cd", "ac", "dc", "ca", "zz", "31114"]

count = 0

for i in range(len(word) - 1):
    for j in range(i + 1, len(word)):
        if word[i] == word[j] or word[i] == word[j][::-1]:
            count += 1

print(count)
