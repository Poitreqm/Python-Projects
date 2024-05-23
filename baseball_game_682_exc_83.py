#
# 682. Baseball Game
# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
#


ops = ["5", "2", "C", "D", "+"]

arr_result = []


for i in range(len(ops)):
    if ops[i] == "C":

        arr_result.pop()
    elif ops[i] == "D":
        arr_result.append(arr_result[-1] * 2)

    elif ops[i] == "+":

        arr_result.append(int(arr_result[-2]) + arr_result[-1])

    elif int(ops[i]):
        arr_result.append(int(ops[i]))


print(sum(arr_result))
