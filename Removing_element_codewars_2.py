# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!



arr = ["Keep", "Remove", "Keep", "Remove", "Keep"]
new_a = []

for i in arr[::2]:
    new_a.append(i)
print(new_a)