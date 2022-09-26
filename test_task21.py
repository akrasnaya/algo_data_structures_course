import unittest
from task21 import SimpleGraph, Vertex

def create_graph_to_test():
    graph1 = SimpleGraph(5)
    graph1.AddVertex('A')
    graph1.AddVertex('B')
    graph1.AddVertex('C')
    graph1.AddVertex('D')
    graph1.AddVertex('E')
    graph1.AddEdge(0, 1)
    graph1.AddEdge(0, 2)
    graph1.AddEdge(0, 3)
    graph1.AddEdge(1, 3)
    graph1.AddEdge(1, 4)
    graph1.AddEdge(2, 3)
    graph1.AddEdge(3, 4)
    return graph1