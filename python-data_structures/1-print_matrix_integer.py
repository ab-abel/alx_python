#!/usr/bin/env python3


def print_matrix_integer(matrix=[[]]):
    
    new_mat = [num for elem in matrix for num in elem]
    for i in range(3, len(new_mat) + 3, 4):
        new_mat.insert(i, '$')
        # print(i, end=" ")
    if len(new_mat) == 0:
        new_mat.append('$')
    
    print_2=""
    for i in range(len(new_mat)):        
        print("{}".format(new_mat[i]), end='')
         
vec = [[1,2,3], [4,5,6], [7,8,9]]

print_matrix_integer(vec)
print_matrix_integer("--")
print_matrix_integer()