#
# 804. Unique Morse Code Words
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.
#

morse = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
]


alphabet = "abcdefghijklmnopqrstuvwxyz"

words = ["a"]

transformations = set()

for i in words:
    word_morse = []
    for j in range(len(i)):
        word_morse.append(morse[alphabet.index(i[j])])
    trs = "".join(word_morse)
    transformations.add(trs)


print(len(transformations))
