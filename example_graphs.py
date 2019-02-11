

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
    2: [1, 6],
    3: [1],
    4: [1, 2, 5],
    5: [1, 3],
    6: [0]
}

adjacency_list_2 = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1],
    3: [0, 1],
    4: []
}

complete_graph = {
    "a": ["b", "c"],
    "b": ["a", "c"],
    "c": ["a", "b"]
}

isolated_graph = {
    "a": [],
    "b": [],
    "c": []
}

disconnected_graph = {
    "a" : ["d"],
    "b" : ["c"],
    "c" : ["b", "c", "d", "e"],
    "d" : ["a", "c"],
    "e" : ["c"],
    "f" : []
}

connected_graph_1 = {
    "a" : ["d","f"],
    "b" : ["c"],
    "c" : ["b", "c", "d", "e"],
    "d" : ["a", "c"],
    "e" : ["c"],
    "f" : ["a"]
}

connected_graph_2 = {
    "a" : ["d","f"],
    "b" : ["c","b"],
    "c" : ["b", "c", "d", "e"],
    "d" : ["a", "c"],
    "e" : ["c"],
    "f" : ["a"]
}


