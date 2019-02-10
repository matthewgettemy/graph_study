"""
Credit to:
https://www.python-course.eu/graphs_python.php
for code examples and data structures.
"""

import example_graphs


def generate_directed_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges


def generate_unique_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            if not sorted((node, neighbor)) in edges:
                edges.append(sorted((node, neighbor)))
    return edges


def find_isolated_nodes(graph):
    isolated_nodes = []
    for node in graph:
        if not graph[node]:
            isolated_nodes.append(node)
    return isolated_nodes


def main():
    edges = generate_directed_edges(example_graphs.adjacency_list_1)
    print(edges)
    edges = generate_directed_edges(example_graphs.adjacency_list_2)
    print(edges)

    edges = generate_unique_edges(example_graphs.adjacency_list_1)
    print(edges)
    edges = generate_unique_edges(example_graphs.adjacency_list_2)
    print(edges)

    isolated_nodes = find_isolated_nodes(example_graphs.adjacency_list_1)
    print(isolated_nodes)
    isolated_nodes = find_isolated_nodes(example_graphs.adjacency_list_2)
    print(isolated_nodes)

if __name__ == '__main__':
    main()