import unittest
from task23 import SimpleGraph, Vertex

def create_graph_with_weak():
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

def create_graph_without_weak():
    graph1 = SimpleGraph(4)
    graph1.AddVertex('A')
    graph1.AddVertex('B')
    graph1.AddVertex('C')
    graph1.AddVertex('D')
    graph1.AddEdge(0, 1)
    graph1.AddEdge(0, 2)
    graph1.AddEdge(1, 2)
    graph1.AddEdge(1, 3)
    graph1.AddEdge(2, 3)



class TestWeakVers(unittest.TestCase):

    def test_find_weak(self):
        graph = create_graph_with_weak()
        weaks = [vert.Value for vert in graph.WeakVertices()]
        self.assertListEqual(weaks, ['E', 'I', 'K'])

    def test_not_find_weak(self):
        graph1 = SimpleGraph(4)
        graph1.AddVertex('A')
        graph1.AddVertex('B')
        graph1.AddVertex('C')
        graph1.AddVertex('D')
        graph1.AddEdge(0, 1)
        graph1.AddEdge(0, 2)
        graph1.AddEdge(1, 2)
        graph1.AddEdge(1, 3)
        graph1.AddEdge(2, 3)
        weaks = graph1.WeakVertices()
        self.assertListEqual(weaks, [])

