#!/usr/bin/env python3
# Return the square of a given matrix

def square_matrix_simple(matrix=[]):
    row_len = len(matrix)
    column_len = len(matrix[0])
    new_mat =[]
    for i in range(row_len):
        new_mat.append([matrix[i][j] **2 for j in range(column_len)])
    return new_mat
