# 2951. Find the Peaks
# You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.
# Return an array that consists of indices of peaks in the given array in any order.
# Notes:
# A peak is defined as an element that is strictly greater than its neighboring elements.
# The first and last elements of the array are not a peak.


mountain = [1, 4, 3, 8, 5]

arr = []

for i in range(0, len(mountain)):
    if i != 0 and i != len(mountain) - 1:
        if mountain[i - 1] < mountain[i] > mountain[i + 1]:
            arr.append(i)

print(arr)
