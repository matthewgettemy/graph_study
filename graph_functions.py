"""
Credit to:
https://www.python-course.eu/graphs_python.php
for code examples and data structures.
"""

import example_graphs
import itertools
import pygraph

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
        return 'Graph("{}")'.format(repr(self.adjacency_list))

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

    def eccentricity(self, vertex):
        pass

    def vertex_degree(self, vertex):
        adjacent_vertices = self.adjacency_list[vertex]
        degree = len(adjacent_vertices) + adjacent_vertices.count(vertex)
        return degree

    def min_degree(self):
        return min([self.vertex_degree(vertex) for vertex in self.adjacency_list])

    def max_degree(self):
        return max([self.vertex_degree(vertex) for vertex in self.adjacency_list])

    def find_isolated_vertices(self):
        isolated_vertices = []
        for node in self.adjacency_list:
            if not self.adjacency_list[node]:
                isolated_vertices.append(node)
        return isolated_vertices

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

    def degree_sequence(self):
        seq = [self.vertex_degree(vertex)
               for vertex in self.vertices()]
        seq.sort(reverse=True)
        return tuple(seq)

    def is_graphic(self):
        """http://mathworld.wolfram.com/GraphicSequence.html"""
        dseq = self.degree_sequence()
        if sum(dseq) % 2:
            return False
        if self.is_degree_sequence(dseq):
            for k in range(1, len(dseq) + 1):
                left = sum(dseq[:k])
                right = k * (k - 1) + sum([min(x, k) for x in dseq[k:]])
                if left > right:
                    return False
        else:
            return False
        return True

    def density(self):
        g = self.adjacency_list
        v = len(g.keys())
        e = len(self.unique_edges())
        return 2.0 * e / (v * (v - 1))

    def is_connected(self, vertices_encountered=None, start_vertex=None):
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.adjacency_list
        vertices = list(gdict.keys())  # "list" necessary in Python 3
        if not start_vertex:
            # chose a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False

    def diameter(self):
        if not self.is_connected():
            # should technically be infinity
            return None
        vertices = self.vertices()
        pairs = itertools.combinations(vertices, 2)
        smallest_paths = []
        for (s, e) in pairs:
            paths = self.find_all_paths(s, e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)
        smallest_paths.sort(key=len)
        diameter = len(smallest_paths[-1]) - 1
        return diameter

    @staticmethod
    def is_degree_sequence(sequence):
        # check if the sequence sequence is non-increasing:
        return all(x >= y for x, y in zip(sequence, sequence[1:]))

def main():
    edges = generate_directed_edges(example_graphs.adjacency_list_1)
    print(edges)
    edges = generate_directed_edges(example_graphs.adjacency_list_2)
    print(edges)

    edges = generate_unique_edges(example_graphs.adjacency_list_1)
    print(edges)
    edges = generate_unique_edges(example_graphs.adjacency_list_2)
    print(edges)


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

    for vertex in g1:
        degree = g1.vertex_degree(vertex)
        print('Vertex {} has degree: {}.'.format(vertex, degree))

    isolated_nodes = find_isolated_nodes(example_graphs.adjacency_list_1)
    print('Isolated Nodes: {}'.format(isolated_nodes))
    isolated_nodes = find_isolated_nodes(example_graphs.adjacency_list_2)
    print('Isolated Nodes: {}'.format(isolated_nodes))

    print('Max degree: {}'.format(g1.max_degree()))
    print('Min degree: {}'.format(g1.min_degree()))
    print('Degree sequence: {}'.format(g1.degree_sequence()))
    print('Is graphic: {}'.format(g1.is_graphic()))
    print('Density: {}'.format(g1.density()))

    graph = Graph(example_graphs.complete_graph)
    print('Complete graph density: {}.'.format(graph.density()))
    graph = Graph(example_graphs.isolated_graph)
    print('Isolated graph density: {}.'.format(graph.density()))

    graph = Graph(example_graphs.disconnected_graph)
    print('Is connected: {}.'.format(graph.is_connected()))
    graph = Graph(example_graphs.connected_graph_1)
    print('Is connected: {}.'.format(graph.is_connected()))
    graph = Graph(example_graphs.connected_graph_2)
    print('Is connected: {}.'.format(graph.is_connected()))

    g1.pop(100)
    g1.pop(101)
    g1.pop(102)
    g1.pop(50)
    print(g1)
    print('PATH: {}'.format(g1.find_path(0, 6)))
    print('CONNECTED: {}'.format(g1.is_connected()))
    print('Diameter: {}.'.format(g1.diameter()))



if __name__ == '__main__':
    main()



