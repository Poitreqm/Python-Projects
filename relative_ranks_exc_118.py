# 506. Relative Ranks
# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.


score = [10, 3, 8, 9, 4]
array_tmp = []
ans = []
res = []
for i in score:
    array_tmp.append(i)

for i in range(len(array_tmp)):
    for j in range(len(array_tmp)):
        if array_tmp[i] > array_tmp[j]:
            tmp = array_tmp[i]
            array_tmp[i] = array_tmp[j]
            array_tmp[j] = tmp


for i in range(len(score)):
    if i == 0:
        ans.append(array_tmp.index(score[i]) + 1)
    elif i == 1:
        ans.append(array_tmp.index(score[i]) + 1)
    elif i == 2:
        ans.append(array_tmp.index(score[i]) + 1)
    else:
        ans.append(array_tmp.index(score[i]) + 1)


for i in ans:
    if i == 1:
        res.append("Gold Medal")
    elif i == 2:
        res.append("Silver Medal")
    elif i == 3:
        res.append("Bronze Medal")
    else:
        res.append(f"{i}")


print(res)
