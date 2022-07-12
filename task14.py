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
            # New item is greater or equal,
            # go right until spot is found
            elif node.RightChild == None:
                node.RightChild = new_node
                new_node.Parent = node.RightChild
            else:
                recurse(node.right)
            # End of recurse

        # Tree is empty, so new item goes at the root
        if self.Root is None:
            self.Root = new_node
        # Otherwise, search for the item's spot
        else:
            recurse(self.Root)

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode

        def rec_min_max(node):
            if node is not None:
                if FindMax:
                    if node.RightChild is None:
                        return node
                    rec_min_max(node.RightChild)
                else:
                    if node.LeftChild is None:
                        return node
                    rec_min_max(node.LeftChild)


        return rec_min_max(FromNode)

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        def delete_node(node, dir):
            if dir == 'right':
                new_node = node.RightChild.RightChild
                if new_node is not None:
                    node.RightChild = new_node
                    new_node.Parent = node
                    delete_node(new_node, 'right')
                else:
                    node.RightChild = None
            else:
                new_node = node.LeftChild.LeftChild
                if new_node is not None:
                    node.LeftChild = new_node
                    new_node.Parent = node
                    delete_node(new_node, 'left')
                else:
                    node.LeftChild = None


        def find_node(node):
            count = 0
            if node is not None:
                if node.RightChild.NodeKey == key:
                    count += 1
                    delete_node(node, 'right')
                find_node(node.RightChild)
                if node.LeftChild.NodeKey == key:
                    count += 1
                    delete_node(node, 'left')
                find_node(node.LeftChild)

            if count != 0:
                return False

        if self.Root is None:
            return 
        if self.Root.NodeKey == key:
            delete_node(self.Root, 'right')
        else:
            find_node(self.Root)


    def Count(self):
        count = 0

        def recurse(node):
            if node is not None:
                count += 1
                recurse(node.LeftChild)
                recurse(node.RightChild)

        recurse(self.Root)
        return count


