class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        if self.Root is None:
            return
        nodes = []
        nodes.append(self.Root)
        all_nodes = []
        while len(nodes) > 0:
            node = nodes.pop()
            all_nodes.append(node)
            if len(node.Children) != 0:
                for child in node.Children:
                    nodes.append(child)


        return all_nodes

    def FindNodesByValue(self, val):
        if self.Root is None:
            return
        nodes = []
        val_nodes = []
        nodes.append(self.Root)
        while len(nodes) > 0:
            node = nodes.pop()
            if node.NodeValue == val:
                val_nodes.append(node)
            if len(node.Children) != 0:
                for child in node.Children:
                    nodes.append(child)

        return val_nodes

    def MoveNode(self, OriginalNode, NewParent):
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent.Children.remove(OriginalNode)

    def Count(self):
        if self.Root is None or len(self.Root.Children) == 0:
            return 0
        count_knit = 0
        nodes = []
        nodes.append(self.Root)
        while len(nodes) > 0:
            node = nodes.pop()
            if len(node.Children) != 0:
                count_knit += 1
                for child in node.Children:
                    nodes.append(child)

        return count_knit


    def LeafCount(self):
        # количество листьев в дереве
        if self.Root is None:
            return 0
        if len(self.Root.Children) == 0:
            return 1
        count_leaves = 0
        nodes = []
        nodes.append(self.Root)
        while len(nodes) > 0:
            node = nodes.pop()
            if len(node.Children) != 0:
                for child in node.Children:
                    nodes.append(child)
            else:
                count_leaves += 1

        return count_leaves

    def EvenTrees(self):
        nodes = self.GetAllNodes()
        total_num = len(nodes)
        tree_matrix = [[0] * total_num for _ in range(total_num)]

        for i in range(len(nodes)):
            if len(nodes[i].Children) != 0:
                for child in nodes[i].Children:
                    child_ind = nodes.index(child)
                    tree_matrix[i][child_ind], tree_matrix[child_ind][i] = 1, 1

        def find_link_to_break(tree, visited, res, node):
            num, temp = 0, 0
            visited[node] = 1

            for i in range(len(tree[node])):
                if visited[tree[node][i]] == 0:
                    temp = find_link_to_break(tree, visited, res, tree[node][i])
                    if temp % 2  == 0:
                        num += temp
                    else:
                        res.append(node)
                        res.append(i)
            return num + 1


        visited = [0] * total_num
        nodes_to_break_link = []
        find_link_to_break(tree_matrix, visited, nodes_to_break_link, 0)
        result = [nodes[i].NodeValue for i in nodes_to_break_link]

        return result
