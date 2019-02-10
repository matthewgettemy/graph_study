

import numpy as np


"""
There are essentially two ways that you can represent a graph: an adjacency
list or an adjacency matrix.
"""


"""Directed graph"""
adjacency_matrix_1 = np.array([
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
])

"""Undirected graph"""
adjacency_matrix_2 = np.array([
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
])


adjacency_list_1 = {
    0: [1, 4],
    1: [3, 4],
    2: [1],
    3: [1],
    4: [1, 2, 5],
    5: [1, 3],
    6: [],
    7: []
}

adjacency_list_2 = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1],
    3: [0, 1],
    4: []
}