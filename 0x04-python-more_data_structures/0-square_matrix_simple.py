#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    j = 0
    for numList in matrix[j]:
        new_matrix.append(list(map((lambda x: x**2), matrix[j])))
        j += 1
    return (new_matrix)
