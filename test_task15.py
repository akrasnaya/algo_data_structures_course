import unittest
from task15 import *

def create_full_tree_to_test():
    tree = aBST(1)
    tree.Tree = [10, 8, 12, 6, 9, 11, 14]
    return tree

def create_sparse_tree_to_test():
    tree = aBST(3)
    tree.Tree = [10, 8, 12, None, 9, None, 14, None, None, None, None, None, None, None, None]
    return tree

def create_empty_tree_to_test():
    tree = aBST(0)
    tree.Tree = [None]
    return tree

class TestABST(unittest.TestCase):

    def test_find_existing_key(self):
        full_tree = create_full_tree_to_test()
        self.assertEqual(full_tree.FindKeyIndex(12), 2)
        sparse_tree = create_sparse_tree_to_test()
        self.assertEqual(sparse_tree.FindKeyIndex(9), 4)

    def test_find_unexisting_key_full_tree(self):
        full_tree = create_full_tree_to_test()
        self.assertEqual(full_tree.FindKeyIndex(15), None)
        self.assertEqual(full_tree.FindKeyIndex(0), None)

    def test_find_unexisting_key_sparse_tree(self):
        sparse_tree = create_sparse_tree_to_test()
        self.assertEqual(sparse_tree.FindKeyIndex(0), -1)
        self.assertEqual(sparse_tree.FindKeyIndex(11), -2)
        self.assertEqual(sparse_tree.FindKeyIndex(80), None)

    def test_find_unexisting_key_empty_tree(self):
        empty_tree = create_empty_tree_to_test()
        self.assertEqual(empty_tree.FindKeyIndex(15), 0)

    def test_add_key_full_tree(self):
        full_tree = create_full_tree_to_test()
        self.assertEqual(full_tree.AddKey(15), -1)
        self.assertEqual(full_tree.AddKey(12), 2)

    def test_add_key_sparse_tree(self):
        sparse_tree = create_sparse_tree_to_test()
        self.assertEqual(sparse_tree.AddKey(9), 4)
        self.assertEqual(sparse_tree.AddKey(5), 3)
        self.assertEqual(sparse_tree.AddKey(16), 14)
        self.assertEqual(sparse_tree.AddKey(20), -1)

    def test_add_key_empty_tree(self):
        empty_tree = create_empty_tree_to_test()
        self.assertEqual(empty_tree.AddKey(10), 0)




if __name__ == '__main__':
    unittest.main()

