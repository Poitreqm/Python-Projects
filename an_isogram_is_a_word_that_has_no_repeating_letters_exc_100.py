# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

s = "zxcsasd".lower()


b = True

for i in s:
    if s.count(i) != 1:
        b = False
        break

print(b)
