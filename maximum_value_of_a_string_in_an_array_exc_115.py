# 2496. Maximum Value of a String in an Array
# The value of an alphanumeric string can be defined as:
# The numeric representation of the string in base 10, if it comprises of digits only.
# The length of the string, otherwise.
# Given an array strs of alphanumeric strings, return the maximum value of any string in strs.


strs = ["1", "01", "001", "0001"]

arr = []
for i in range(len(strs)):

    if strs[i].isdigit():
        arr.append(int(strs[i]))
        print(str(strs[i]))
    else:
        arr.append(len(strs[i]))
        print(len(strs[i]))

print(max(arr))
