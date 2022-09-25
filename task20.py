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
        def calculate_count(node):
            if node is None:
                return 0
            count = 1
            for child in node.Children:
                count += calculate_count(child)
            return count

        return calculate_count(self.Root)


    def LeafCount(self):
        # количество листьев в дереве
        if self.Root is None:
            return 0
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

    def create_matrix_from_tree(self):
        size = self.Count()
        nodes = self.GetAllNodes()
        tree_matrix = [[] for _ in range(size + 2)]
        for i in range(len(nodes)):
            #if len(nodes[i].Children) != 0:
            for child in nodes[i].Children:
                child_ind = nodes.index(child)
                tree_matrix[i].append(child.NodeValue)
                tree_matrix[child_ind].append(nodes[i].NodeValue)
        return tree_matrix

    def EvenTrees(self):
        nodes = self.GetAllNodes()
        total_num = self.Count()
        tree_matrix = self.create_matrix_from_tree()
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
                        #res.append(i)
            return  num + 1


        visited = [0] * (total_num + 2)
        nodes_to_break_link = []
        find_link_to_break(tree_matrix, visited, nodes_to_break_link, 0)
        result = [node for node in nodes_to_break_link][:2]
        fin = []
        for i in result:
            for node in nodes:
                if node.NodeValue == 1 or node.NodeValue == i:
                    fin.append(node)

        return fin