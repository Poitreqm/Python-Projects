#
# 2942. Find Words Containing Character
# You are given a 0-indexed array of strings words and a character x.
# Return an array of indices representing the words that contain the character x.
# Note that the returned array may be in any order
#

words = ["leet", "code", "cod"]
x = "e"

arr = []

for i in range(len(words)):
    if x in words[i]:
        arr.append(i)

# for i in words:   это не работает с некоторыми вариантами
#     if x in i:
#         arr.append(i)

print(arr)
