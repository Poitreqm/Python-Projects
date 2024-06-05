# Maximum number of candies
# An array of costs is given, where the cost of i candy is in i place.
# The boy has coins of coins and he wants to buy as many candies as possible. What is the maximum number of candies a boy can buy?


costs = [1, 3, 2, 4, 1]
coins = 7


r = []

for i in range(0, len(costs)):
    if not costs[i] + sum(r) > coins:
        r.append(costs[i])

print(len(r))
