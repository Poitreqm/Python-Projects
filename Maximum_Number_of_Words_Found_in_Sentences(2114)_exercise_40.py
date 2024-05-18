#
# 2114. Maximum Number of Words Found in Sentences
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.
#


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

max_len = 0
for i in range(len(sentences)):
    if max_len < len(sentences[i].split()):
        max_len = len(sentences[i].split())

print(max_len)
