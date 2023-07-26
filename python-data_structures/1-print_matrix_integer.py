#!/usr/bin/env python3



def print_matrix_integer(matrix=[[]]):
    new_mat = [num for elem in matrix for num in elem]
    for i in range(3, len(new_mat) + 3, 4):
        new_mat.insert(i, '$\n')
        # print(i, end=" ")
    if len(new_mat) == 0:
        new_mat.append('$')
    # print(new_mat)
    new_mat  =''.join(['{:2d}'.format(i) if type(i) == int else str(i) for i in new_mat])
    print(new_mat)

# vec = [[1,2,3], [4,5,6], [7,8,9]]

# print_matrix_integer(vec)
# print_matrix_integer("--")
# print_matrix_integer()