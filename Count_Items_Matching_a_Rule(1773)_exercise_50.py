#
# 1773. Count Items Matching a Rule
# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
# The ith item is said to match the rule if one of the following is true:
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.
#

items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "phone"],
    ["phone", "gold", "iphone"],
]

arr_rule_key = ["type", "color", "name"]
ruleKey = "type"
ruleValue = "phone"

count = 0
rule_index = arr_rule_key.index(ruleKey)
for i in items:
    if i[rule_index] == ruleValue:
        count += 1
print(count)
