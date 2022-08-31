#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_size = len(matrix)
    new_matrix = [None] * matrix_size
    j = 0
    for numList in matrix[j]:
        new_matrix[j] = (list(map((lambda x: x**2), matrix[j])))
        j += 1
    return (new_matrix)
