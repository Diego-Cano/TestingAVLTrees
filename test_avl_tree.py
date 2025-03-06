# test_avl_tree.py
import unittest
from avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):

    def setUp(self):
        """Initialize a new AVL Tree before each test."""
        self.tree = AVLTree()

    def test_insert_simple(self):
        """Test inserting without requiring rotations."""
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.assertEqual(self.tree.in_order_traversal(), [10, 20, 30])

    def test_insert_rotations(self):
        """Test insertions that require rotations."""
        self.tree.insert(30)
        self.tree.insert(20)
        self.tree.insert(10)  # Should trigger right rotation
        self.assertEqual(self.tree.in_order_traversal(), [10, 20, 30])

        self.tree.insert(40)
        self.tree.insert(50)  # Should trigger left rotation
        self.assertEqual(self.tree.in_order_traversal(), [10, 20, 30, 40, 50])

    def test_delete_leaf(self):
        """Test deleting a leaf node."""
        self.tree.insert(20)
        self.tree.insert(10)
        self.tree.insert(30)
        self.tree.delete(10)
        self.assertEqual(self.tree.in_order_traversal(), [20, 30])

    def test_delete_with_one_child(self):
        """Test deleting a node with one child."""
        self.tree.insert(20)
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.delete(10)
        self.assertEqual(self.tree.in_order_traversal(), [5, 20])

    def test_delete_with_two_children(self):
        """Test deleting a node with two children."""
        self.tree.insert(30)
        self.tree.insert(20)
        self.tree.insert(40)
        self.tree.insert(35)
        self.tree.insert(50)
        self.tree.delete(40)  # Should replace with inorder successor
        self.assertEqual(self.tree.in_order_traversal(), [20, 30, 35, 50])

    def test_search(self):
        """Test search operation."""
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.assertTrue(self.tree.search(20))
        self.assertFalse(self.tree.search(100))

if __name__ == '__main__':
    unittest.main()
