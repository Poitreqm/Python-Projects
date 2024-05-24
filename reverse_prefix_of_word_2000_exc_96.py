# 2000. Reverse Prefix of Word
# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
# If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.


word = "abcdefd"
ch = "d"
s = ""

b = False
if ch in word:
    n = word.index(ch)
    for i in reversed(range(n + 1)):
        s = s + word[i]

    s = s + word[n:]

else:
    s = word
    b = True

if b == False:
    s = s[: word.index(ch) + 1] + s[word.index(ch) + 2 :]
else:
    print(s)

print(s)
