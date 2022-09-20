#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix

    Args:
        m_a (double list): First matrix
        m_b (double list): second matrix

    Returns:
        The product of m_a and m_b

    """
    return np.matmul(m_a, m_b)
