class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, value):
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        new_vertex = Vertex(value)
        ind = self.vertex.index(None)
        self.vertex[ind] = new_vertex
        pass

        # здесь и далее, параметры v -- индекс вершины

    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        self.vertex[v] = None
        self.m_adjacency[v] = [0] * len(self.m_adjacency[v])
        for row in self.m_adjacency:
            row[v] = 0

        pass

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
            return True
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = 1, 1
        pass

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = 0, 0
        pass

    def GetClosestVerts(self, v):
        verts = []
        for vert in self.vertex:
            if vert is not None and self.IsEdge(self.vertex.index(vert), v):
                verts.append(vert)
        return verts


    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        path = []
        for vert in self.vertex:
            vert.Hit = False

        def find_path(v, VTo):
            current = self.vertex[v]
            current.Hit = True
            path.append(current)
            if self.IsEdge(v, VTo):
                path.append(self.vertex[VTo])
                return path
            for neighbour in self.GetClosestVerts(v):
                if not neighbour.Hit:
                    return find_path(self.vertex.index(neighbour), VTo)
            path.pop()
            return []
        return find_path(VFrom, VTo)





        

