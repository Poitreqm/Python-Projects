# 867. Transpose Matrix
# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_matrix = [list(row) for row in zip(*matrix)]


print(new_matrix)
