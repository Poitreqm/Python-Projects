# 2085. Count Common Words With One Occurrence
# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

words1 = ["a", "ab"]
words2 = ["a", "a", "a", "ab"]

res = set()

for i in words1:
    if words1.count(i) == 1 and words2.count(i) == 1:
        res.add(i)

for j in words2:
    if words2.count(j) == 1 and words1.count(j) == 1:
        res.add(j)

print(len(res))
