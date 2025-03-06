# avl_tree.py

class Node:
    """Represents a node in the AVL tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New nodes start with height 1

class AVLTree:
    """AVL Tree implementation supporting insertion, deletion, and search."""
    
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        """Returns the height of a node, or 0 if None."""
        return node.height if node else 0

    def _get_balance_factor(self, node):
        """Returns the balance factor (left height - right height)."""
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _rotate_right(self, z):
        """Performs a right rotation."""
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = max(self._get_height(z.left), self._get_height(z.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1

        return y

    def _rotate_left(self, z):
        """Performs a left rotation."""
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = max(self._get_height(z.left), self._get_height(z.right)) + 1
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1

        return y

    def _balance(self, node):
        """Balances a node and returns the new root."""
        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1:  # Left Heavy
            if self._get_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)  # Left-Right Case
            return self._rotate_right(node)

        if balance_factor < -1:  # Right Heavy
            if self._get_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)  # Right-Left Case
            return self._rotate_left(node)

        return node  # Already balanced

    def _insert(self, node, key):
        """Recursively inserts a key and balances the tree."""
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # Duplicate keys not allowed

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        return self._balance(node)

    def insert(self, key):
        """Public method to insert a key."""
        self.root = self._insert(self.root, key)

    def _min_value_node(self, node):
        """Finds the node with the smallest key (leftmost)."""
        while node.left:
            node = node.left
        return node

    def _delete(self, node, key):
        """Recursively deletes a key and balances the tree."""
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children: get inorder successor (smallest in right subtree)
            temp = self._min_value_node(node.right)
            node.key = temp.key  # Copy successor's value to this node
            node.right = self._delete(node.right, temp.key)  # Delete successor

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        return self._balance(node)

    def delete(self, key):
        """Public method to delete a key."""
        self.root = self._delete(self.root, key)

    def search(self, key):
        """Search for a key in the AVL tree."""
        def _search(node, key):
            if not node:
                return False
            if key == node.key:
                return True
            return _search(node.left, key) if key < node.key else _search(node.right, key)

        return _search(self.root, key)

    def in_order_traversal(self):
        """Returns the in-order traversal of the AVL tree (sorted order)."""
        result = []
        def _in_order(node):
            if node:
                _in_order(node.left)
                result.append(node.key)
                _in_order(node.right)

        _in_order(self.root)
        return result
