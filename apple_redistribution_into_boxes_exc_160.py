# You are given an array apple of size n and an array capacity of size m.
# There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.
# Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.
# Note that, apples from the same pack can be distributed into different boxes.

apple = [5, 5, 5]
capacity = [2, 4, 2, 7]

capacity.sort(reverse=True)

res = []

for i in range(len(capacity)):
    while sum(apple) > sum(res):
        res.append(capacity[i])
        capacity.remove(capacity[i])
print(len(res))
