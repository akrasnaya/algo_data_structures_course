class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

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
        if self.Root is None:
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
