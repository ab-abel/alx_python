def create_square_display_with_spaces(size):
    for i in range(size):
        print(" " * size, end='\n')
    for i in range(size):
            for j in range(size):
                print(" ", end="")
            for j in range(size):
                print("*", end="")
            print()

# Change the value of 'size' to adjust the size of the square display
size = 5
create_square_display_with_spaces(size)