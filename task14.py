class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        result = BSTFind()
        if self.Root is None:
            return result

        def recurse(node):
            if node is None:
                result.ToLeft = True
                return result
            elif key == node.NodeKey:
                result.Node = node
                result.NodeHasKey = True
                return result
            elif key < node.NodeKey:
                return recurse(node.LeftChild)
            else:
                return recurse(node.RightChild)
        # ищем в дереве узел и сопутствующую информацию по ключу
        return recurse(self.Root) # возвращает BSTFind

    def AddKeyValue(self, key, val):

        new_node = BSTNode()
        new_node.NodeKey = key
        new_node.NodeValue = val

        def recurse(node):
            # New item is less, go left until spot is found
            if key == node.NodeKey:
                return False
            elif key < node.NodeKey:
                if node.LeftChild == None:
                    node.LeftChild = new_node
                    new_node.Parent = node.LeftChild
                else:
                    recurse(node.left)

            elif node.RightChild == None:
                node.RightChild = new_node
                new_node.Parent = node.RightChild
            else:
                recurse(node.right)

        if self.Root is None:
            self.Root = new_node

        else:
            recurse(self.Root)

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode

        current = FromNode
        if FindMax:
            while current.RightChild is not None:
                current = current.RightChild
        else:
            while current.LeftChild is not None:
                current = current.LeftChild

        return current

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        if self.Root is None:
            return 

        search = self.FindNodeByKey(key)
        if not search.NodeHasKey:
            return False
        
        if self.Root.NodeKey == key and self.Root.LeftChild is None and self.Root.RightChild is None:
            self.Root = None
            return True


        def deleteNode(node, key):
            if node is None:
                return 
            if key < node.NodeKey:
                node.LeftChild = deleteNode(node.LeftChild, key)

            elif key > node.NodeKey:
                node.RightChild = deleteNode(node.RightChild, key)
            else:
                if node.LeftChild is None:
                    temp = node.RightChild
                    node = None
                    return temp
                elif node.RightChild is None:
                    temp = node.LeftChild
                    node = None
                    return temp

                temp = self.FinMinMax(node.RightChild, False)

                node.NodeKey = temp.NodeKey

                node.RightChild = deleteNode(node.RightChild, temp.NodeKey)

            return node

        return deleteNode(self.Root, key)

    
    def Count(self):
        if self.Root is None:
            return 0
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node.LeftChild) + count_nodes(node.RightChild)
        return count_nodes(self.Root)


