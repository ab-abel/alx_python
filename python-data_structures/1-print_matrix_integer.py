#!/usr/bin/env python3


def print_matrix_integer(matrix=[[]]):
    new_mat = [num for elem in matrix for num in elem]
    for i in range(3, len(new_mat) + 3, 4):
        new_mat.insert(i, '$\n')
        # print(i, end=" ")
    if len(new_mat) == 0:
        new_mat.append('$')
    return new_mat
