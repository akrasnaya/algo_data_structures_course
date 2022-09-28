import unittest
from task22 import SimpleGraph, Vertex

def create_graph_to_test():
    graph1 = SimpleGraph(10)
    graph1.AddVertex('A')
    graph1.AddVertex('B')
    graph1.AddVertex('C')
    graph1.AddVertex('D')
    graph1.AddVertex('E')
    graph1.AddVertex('F')
    graph1.AddVertex('G')
    graph1.AddVertex('H')
    graph1.AddVertex('I')
    graph1.AddVertex('K')
    graph1.AddEdge(0, 1)
    graph1.AddEdge(0, 2)
    graph1.AddEdge(0, 4)
    graph1.AddEdge(1, 2)
    graph1.AddEdge(1, 3)
    graph1.AddEdge(2, 5)
    graph1.AddEdge(3, 2)
    graph1.AddEdge(4, 5)
    graph1.AddEdge(5, 6)
    graph1.AddEdge(5, 7)
    graph1.AddEdge(6, 7)
    graph1.AddEdge(7, 8)
    return graph1

class TestTreeSearch(unittest.TestCase):
    def test_shortest_paths(self):
        graph = create_graph_to_test()
        path = [vertex.Value for vertex in graph.BreadthFirstSearch(2, 5)]
        self.assertEqual(path, ['C', 'F'])

    def test_longer_path(self):
        graph = create_graph_to_test()
        path = [vertex.Value for vertex in graph.BreadthFirstSearch(2, 7)]
        self.assertListEqual(path, ['C', 'F', 'H'])

    def test_longest_path(self):
        graph = create_graph_to_test()
        path = [vertex.Value for vertex in graph.BreadthFirstSearch(0, 8)]
        self.assertListEqual(path, ['A', 'C', 'F', 'H', 'I'])

    def test_unexisting_path(self):
        graph = create_graph_to_test()
        path = graph.BreadthFirstSearch(0, 9)
        self.assertListEqual(path, [])

