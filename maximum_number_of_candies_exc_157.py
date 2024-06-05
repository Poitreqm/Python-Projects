# Maximum number of candies
# An array of costs is given, where the cost of i candy is in i place.
# The boy has coins of coins and he wants to buy as many candies as possible. What is the maximum number of candies a boy can buy?


costs = [10, 6, 8, 7, 7, 8]
coins = 5


r = []

for i in range(0, len(costs)):
    tmp = costs[i]
    if sum(r) <= coins and min(costs) < coins:
        if not costs[i] + sum(r) > coins:
            r.append(tmp)

print(len(r))
