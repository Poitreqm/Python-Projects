#
# 2185. Counting Words With a Given Prefix
# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.
#

words = ["pay", "attention", "practice", "attend"]
pref = "at"


count = 0
for i in range(len(words)):
    if pref in words[i]:
        for j in range(len(pref)):
            if words[i][j][: (len(pref))] == pref[j]:
                print(words[i][j])
                count = count + 1

# for i in words:
#     if i.startswith(pref):
#         count += 1
# тоже самое

count = count / len(pref)

print(count)
