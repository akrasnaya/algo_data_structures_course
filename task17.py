class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева


    def GenerateTree(self, a):

        sorted_a = sorted(a)
        root_ind = len(sorted_a) // 2
        root = sorted_a[root_ind]
        tree = BalancedBST()
        tree.Root = BSTNode(root, None)
        tree.Root.Level = 0


        def fill_tree(array, ind, parent_node, level):
            left_part = array[:ind]
            if len(left_part) > 0:
                left_centre = len(left_part) // 2
                left_child = BSTNode(left_part[left_centre], parent_node)
                left_child.Level = level + 1
                parent_node.LeftChild = left_child
            right_part = array[ind + 1:]
            if len(right_part) > 0:
                right_centre = len(right_part) // 2
                right_child = BSTNode(right_part[right_centre], parent_node)
                right_child.Level = level + 1
                parent_node.RightChild = right_child
            if len(left_part) > 0:
                fill_tree(left_part, left_centre, left_child, level + 1)
            if len(right_part) > 0:
                fill_tree(right_part, right_centre, right_child, level + 1)

        fill_tree(sorted_a, root_ind, tree.Root, tree.Root.Level)

        return tree




    def IsBalanced(self, root_node):
        if self.Root is None:
            return True

        def calculate_height(parent, dir):
            temp = parent
            while temp is not None:
                height = temp.Level
                if dir == 'left':
                    temp = temp.LeftChild
                else:
                    temp = temp.RightChild
            return height

        left_height = calculate_height(self.Root, 'left')
        right_height = calculate_height(self.Root, 'right')

        if abs(left_height - right_height) > 1:
            return False
        return True
