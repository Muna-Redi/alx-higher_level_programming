#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    mat_len = len(matrix)
    for i in range(mat_len):
        for num in matrix[i]:
            print("{:d}".format(num), end = '')
    print()
