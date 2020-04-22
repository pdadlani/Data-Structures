import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
# hi

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check: if the tree is empty
        if self.value is None:
            # then put node at the root
            self.value = BinarySearchTree(value)
            return

        # otherwise
        # if value of new node < value of root 
        if value < self.value:
            # call insert on the left bst, if there is one; 
            # otherwise instantiate a new BST with this value
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # else if value of new node is >= value of root
        # there is no need to actually check this, but it's nice
        elif value >= self.value:
            # call insert on the right bst, if there is one
            # otherwise, instantiate a new BST with this value
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(7)
bst.insert(5)
bst.insert(8)
bst.insert(4)
bst.insert(6)