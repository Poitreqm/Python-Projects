# Matrix transposition
# The matrix matrix given by the list is given. Write a transp function that will transpose this matrix in the most convenient and elegant way that Python provides.

matrix = [[1, 2, 3], [1, 2, 3]]

r = [[i, j] for i, j in zip(*matrix)]

print(r)
