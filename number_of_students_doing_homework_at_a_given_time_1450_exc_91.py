#
# 1450. Number of Students Doing Homework at a Given Time
# Given two integer arrays startTime and endTime and given an integer queryTime.
# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
# Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
#


startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]
endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10]
queryTime = 5

count = 0
for i in range(len(startTime)):
    if (
        (startTime[i] <= queryTime and endTime[i] >= queryTime)
        or len(startTime) == 1
        and startTime[i] == queryTime
    ):
        count = count + 1


print(count)
