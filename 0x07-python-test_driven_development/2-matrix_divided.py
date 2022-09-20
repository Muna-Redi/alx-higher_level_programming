#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divides a matrix with a divisor

    args:
        matrix (double list): the matrix to be divided with a divisor

        divisor (int/float): matrix divisor

    Returns:
        returns a new matrix of the resulting quotients

    raises:
        TypeError:
        Exceptions----------------------------

        matrix: must be a (list of lists) ints/floats
        also matrix rows must be of the same size

        div: must be an integer or float

    ZeroDivisionError: div can not be zero
    """
    """Alternative code
    a = [[]]
    for i in range(len(matrix)):
        if i == 0:
            a = [list(map(lambda x: round((x/div), 2), matrix[i]))]
        else:
            a.append(list(map(lambda x: round((x/div), 2), matrix[i])))
    return a
    """
    return [list(map(lambda x: round((x/div), 2), matrix[i]))
            for i in range(len(matrix))]
