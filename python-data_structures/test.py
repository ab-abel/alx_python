#!/usr/bin/env python3



def print_matrix_integer(matrix=[[]]):
    new_mat = [num for elem in matrix for num in elem]
    for i in range(3, len(new_mat) + 3, 4):
        new_mat.insert(i, '$\n')
        # print(i, end=" ")
    if len(new_mat) == 0:
        new_mat.append('$')
    # print(new_mat)
    # new_mat  =''.join(['{:2d}'.format(i) if type(i) == int else str(i) for i in new_mat])
    # print(new_mat)

# vec = [[1,2,3], [4,5,6], [7,8,9]]

# print_matrix_integer(vec)
# print_matrix_integer("--")
# print_matrix_integer()





#!/usr/bin/env python3


def print_matrix_integer(matrix=[[]]):
    
    new_mat = [num for elem in matrix for num in elem]
    for i in range(3, len(new_mat) + 3, 4):
        new_mat.insert(i, '$')
        # print(i, end=" ")
    if len(new_mat) == 0:
        new_mat.append('$')
    
    # print(new_mat)
    print_2=""
    # for i in range(len(new_mat)):        
    new_string_mat = ["{:d}".format(i) if type(i) == int else str(i) for i in new_mat]

    i = 1
    print_string=''
    while i < len(new_string_mat)+1:
        # print(new_string_mat[i], end='')
        print(i ,end="")
        
        if i%3 ==0:
            print("$\n", end='') 
            
        else:
            print(" ", end='')
            # pass
            #         
        i +=1
    
         
vec = [[1,2,3], [4,5,6], [7,8,9]]

print_matrix_integer(vec)
print_matrix_integer("--")
print_matrix_integer()

# def print_matrix_integer(matrix=[[]]):
#     for row in matrix:
#         for i, num in enumerate(row):
#             # print(row)
#             print("{}".format(num), end=' ' if i < len(row)-1 else '$')
#         print()

    new_str =''
    for row in new_string_mat:
        for i, num in enumerate(row):
            # print(len(row))
            # print(i)
            print("{}".format(num), end='' if i < len(row) else '')
            if i%3 ==0:
                print('', end='')
    print()


   
    # print(new_mat)
    print_2=""
    # for i in range(len(new_mat)):        
    new_string_mat = ["{:d}".format(i) if type(i) == int else str(i) for i in new_mat]

    # i = 1
    # print_string=''
    # print(new_string_mat)
    # while i < len(new_string_mat)+1:
    #     print(i ,end="")
    #     if i%3 ==0:
    #         print("$\n", end='') 
    #     else:
    #         print(" ", end='') 
    #     i +=1
    
    new_str =''
    # for row in new_string_mat:
    
    for i, num in enumerate(new_string_mat):
        # print("{}".format(num), end='' if i < len(new_string_mat)-1 else '')
        print('{}'.format(num),end='')
        
        # print(i, end='')
        if i%3 ==0:
            print('', end='')
        # else:
        #     print('', end='')
    print()


    new_mat = [num for elem in matrix for num in elem]
    for i in range(3, len(new_mat) + 3, 4):
        new_mat.insert(i, '$')
    if len(new_mat) == 0:
        new_mat.append('$')
 
    return(new_mat)






    def print_matrix_integer(matrix=[[]]):
    new_mat = [num for elem in matrix for num in elem]
    new_string_mat = ["{:d}".format(i) if type(i) == int else str(i) for i in new_mat]
    
    for i in range(3, len(new_string_mat)+1, 3):
        print(new_string_mat[i-3:i], end='$')
    #     print()
    # print(new_mat[0])
    print_str = ''
    for i in new_string_mat:
        print_str += "{:2s}".format(i)
        # print(i)
    # print(print_str)
    # print(len(print_str))


    # print(new_string_mat)

    # for i in new_string_mat:
        



vec = [[1,2,3], [4,5,6], [7,8,9]]
print_matrix_integer(vec)
# print_matrix_integer("--")
# print_matrix_integer()

