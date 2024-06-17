# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:
# Choose the pile with the maximum number of gifts.
# If there is more than one pile with the maximum number of gifts, choose any.
# Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
# Return the number of gifts remaining after k seconds.

import math

gifts = [25, 64, 9, 4, 100]
k = 4

res = gifts.copy()

for i in range(len(gifts)):
    while 0 < k:
        k = k - 1
        gifts[gifts.index(max(gifts))] = int(math.sqrt(gifts[gifts.index(max(gifts))]))

print(int(sum(gifts)))
