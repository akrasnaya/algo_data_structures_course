import unittest
from task20 import SimpleTreeNode
from task20 import SimpleTree

def create_tree_to_test():
    root = SimpleTreeNode(0, None)
    tree1 = SimpleTree(root)
    tree1.AddChild(root, SimpleTreeNode(1, None))
    tree1.AddChild(root, SimpleTreeNode(2, None))
    tree1.AddChild(root, SimpleTreeNode(3, None))
    tree1.AddChild(root.Children[0], SimpleTreeNode(4, None))
    tree1.AddChild(root.Children[0], SimpleTreeNode(5, None))
    tree1.AddChild(root.Children[1], SimpleTreeNode(6, None))
    tree1.AddChild(root.Children[1], SimpleTreeNode(7, None))
    tree1.AddChild(root.Children[2], SimpleTreeNode(8, None))
    tree1.AddChild(root.Children[2], SimpleTreeNode(9, None))
    tree1.AddChild(root.Children[2], SimpleTreeNode(10, None))
    return tree1

def create_empty_tree():
    root = SimpleTreeNode(0, None)
    tree1 = SimpleTree(root)
    return tree1


class TestTree(unittest.TestCase):
    def test_count_nodes_full_tree(self):
        tree = create_tree_to_test()
        self.assertEqual(tree.Count(), 4)

    def test_count_leaves_full_tree(self):
        tree = create_tree_to_test()
        self.assertEqual(tree.LeafCount(), 7)

    def test_count_node_empty_tree(self):
        tree = create_empty_tree()
        self.assertEqual(tree.Count(), 1)

    def test_count_leaves_empty_tree(self):
        tree = create_empty_tree()
        self.assertEqual(tree.LeafCount(), 0)


