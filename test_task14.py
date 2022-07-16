import unittest
from task14 import *

def extract_node_keys(tree):
    keys = []
    def rec(node):
        if node is not None:
            keys.append(node.NodeKey)
            rec(node.LeftChild)
            rec(node.RightChild)
        return keys
    return rec(tree.Root)

def create_tree_to_test():
    root = BSTNode(10, 10, None)
    node1 = BSTNode(8, 8, root) #node
    node2 = BSTNode(12, 12, root) #node
    root.LeftChild = node1
    root.RightChild = node2
    node3 = BSTNode(6, 6, node1) #leaf
    node4 = BSTNode(9, 9, node1) #leaf
    node1.LeftChild = node3
    node1.RightChild = node4
    node5 = BSTNode(11, 11, node2) #leaf
    node6 = BSTNode(14, 14, node2) #leaf
    node2.LeftChild = node5
    node2.RightChild = node6

    tree = BST(root)

    return tree

class TestBST(unittest.TestCase):
    def test_deleting_root(self):
        tree = create_tree_to_test()
        res = tree.DeleteNodeByKey(10)
        self.assertEqual(tree.Root.NodeKey, 11)
        self.assertListEqual(extract_node_keys(tree), [11, 8, 6, 9, 12, 14])
        self.assertEqual(res.NodeKey, 10)

    def test_deleting_node(self):
        tree = create_tree_to_test()
        res = tree.DeleteNodeByKey(8)
        self.assertListEqual(extract_node_keys(tree), [10, 9, 6, 12, 11, 14])
        self.assertEqual(res.NodeKey, 8)

    def test_deleting_leaf(self):
        tree = create_tree_to_test()
        res = tree.DeleteNodeByKey(14)
        self.assertListEqual(extract_node_keys(tree), [10, 8, 6, 9, 12, 11])
        self.assertEqual(res.NodeKey, 14)

    def test_delete_absent_node(self):
        tree = create_tree_to_test()
        res = tree.DeleteNodeByKey(2)
        self.assertEqual(res, False)


if __name__ == '__main__':
    unittest.main()
