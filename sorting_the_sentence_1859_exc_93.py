#
# 1859. Sorting the Sentence
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.
# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
#


s = "is2 sentence4 This1 a3"

arr = s.split(" ")

tmp_indexes = []
res = [0] * len(arr)

for i in range(len(arr)):
    tmp_indexes.append(int(arr[i][-1]) - 1)


for i in range(len(arr)):
    x = tmp_indexes[i]
    res[x] = arr[i]

print(res)

for i in range(len(res)):
    for c in res[i]:
        if c.isdigit():
            res[i] = res[i].replace(c, "")
            break

print(" ".join(res))
