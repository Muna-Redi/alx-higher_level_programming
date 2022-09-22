#!/usr/bin/python3
""" module that multiplies two matrices """


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices

    args:
        m_a (int): First matrix containing integers or floats

        m_b (int): Second matrix containing integers or floats

    return: returns the product of the two matrices

    raises:
        TypeError: 
            m_a or m_b must be a list of lists.
            m_a and m_b must contain only integers or floats.

        ValueError: the matrix can't be empty.
            matrix must have equal rows i.e Rectangular
            m_a and m_b must be multipliable.
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if (len(m_a[0]) > 0) == False:
        raise TypeError("m_a must be a list of lists")

    if (len(m_b[0]) > 0) == False:
        raise TypeError("m_b must be a list of lists")

    size_a = len(m_a[0])
    size_b = len(m_b[0])
    for i in range(len(m_a)):
        if len(m_a[i]) != size_a:
            raise TypeError("each row of M_a must be of the sane size")
    for j in range(len(m_b)):
        if len(m_b[j]) != size_b:
            raise TypeError("each row of M_b must be of the sane size")
    if size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    i = 0
    j = 0
    p_matrix = [[]]

    for i in range(len(m_a)):

        for j in range(len(m_b[i])):
            pmx = 0
            k = 0

            for k in range(len(m_b)):
                pmx += (m_a[i][k]) * (m_b[k][j])

            if i == 0:
                if len(p_matrix[0]) == 0:
                    p_matrix[0] = [pmx]

                else:
                    p_matrix[i].append(pmx)
                    continue

            elif len(p_matrix) < (i+1):
                p_matrix.append([pmx])

            else:
                p_matrix[i].append(pmx)

    return p_matrix
