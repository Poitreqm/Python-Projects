# The sum of disjoint subarrays
# An array of non-negative integers is given. find the maximum sum of two disjoint characters L and M, respectively.

A = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
L = 4
M = 3

A.sort(reverse=True)

arr_l = []
arr_m = []

if L == 1:
    arr_l.append(max(A))
if M == 1:
    arr_m.append(max(A))


for i in range(len(A)):
    tmp = A[i]
    if not len(arr_l) == L and tmp not in arr_l and tmp not in arr_m:
        arr_l.append(tmp)
    elif not len(arr_m) == M and tmp not in arr_l and tmp not in arr_m:
        arr_m.append(tmp)


print(arr_l)
print(arr_m)

print(sum(arr_l) + sum(arr_m))
