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


class Graph:

    def __init__(self, adjacency_list={}):
         self.adjacency_list = adjacency_list

    def __setitem__(self, key, value):
        self.adjacency_list[key] = value

    def __getitem__(self, key):
        return self.adjacency_list[key]

    def __repr__(self):
        return repr(self.adjacency_list)

    def __len__(self):
        return len(self.adjacency_list)

    def __delitem__(self, key):
        del self.adjacency_list[key]

    def clear(self):
        return self.adjacency_list.clear()

    def copy(self):
        return self.adjacency_list.copy()

    def has_key(self, key):
        return key in self.adjacency_list

    def update(self, *args, **kwargs):
        return self.adjacency_list.update(*args, **kwargs)

    def keys(self):
        return self.adjacency_list.keys()

    def values(self):
        return self.adjacency_list.values()

    def items(self):
        return self.adjacency_list.items()

    def pop(self, *args):
        return self.adjacency_list.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.adjacency_list, dict_)

    def __contains__(self, item):
        return item in self.adjacency_list

    def __iter__(self):
        return iter(self.adjacency_list)

    def vertices(self):
        return list(self.adjacency_list.keys())

    def directed_edges(self):
        return self.generate_directed_edges()

    def unique_edges(self):
        return self.generate_unique_edges()

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            print('Adding vertex {}.'.format(vertex))
            self.adjacency_list[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.adjacency_list:
            if vertex2 not in self.adjacency_list[vertex1]:
                print('Adding edge {}:{} to graph.'.format(vertex1, vertex2))
                self.adjacency_list[vertex1].append(vertex2)
            else:
                print('Edge {}:{} already defined in this graph.'
                      .format(vertex1, vertex2))
        else:
            print('Adding edge {}:{} to graph.'.format(vertex1, vertex2))
            self.adjacency_list[vertex1] = [vertex2]

    def generate_unique_edges(self):
        edges = []
        for node in self.adjacency_list:
            for neighbor in self.adjacency_list[node]:
                if not tuple(sorted((node, neighbor))) in edges:
                    edges.append(tuple(sorted((node, neighbor))))
        return edges

    def generate_directed_edges(self):
        edges = []
        for node in self.adjacency_list:
            for neighbor in self.adjacency_list[node]:
                edges.append((node, neighbor))
        return edges

    def find_path(self, start_vertex, end_vertex, path=None):
        if path is None:
            path = []
        graph = self.adjacency_list
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self.adjacency_list
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths:
                    paths.append(p)
        return paths

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

    # Testing the Graph class.
    g1 = Graph(example_graphs.adjacency_list_1)

    print(g1.vertices())
    g1.add_vertex(100)
    g1.add_vertex(101)
    g1.add_vertex(102)
    print(g1.vertices())

    print('Directed edges: {}'.format(g1.directed_edges()))
    print('Unique edges:   {}'.format(g1.unique_edges()))

    g1.add_edge((0, 1))
    g1.add_edge((0, 2))
    g1.add_edge((0, 3))
    print('Directed edges: {}'.format(g1.directed_edges()))
    print('Unique edges:   {}'.format(g1.unique_edges()))

    print(g1[0])
    print(g1[1])
    print(g1[2])

    g1[50] = [1, 2, 3, 4]
    print(g1[50])
    g1[50]= [1]
    print(g1[50])

    path = g1.find_path(0, 4)
    print(path)
    path = g1.find_path(0, 5)
    print(path)
    path = g1.find_path(2, 5)
    print(path)
    path = g1.find_path(5, 2)
    print(path)

    paths = g1.find_all_paths(0, 5)
    print(paths)

if __name__ == '__main__':
    main()