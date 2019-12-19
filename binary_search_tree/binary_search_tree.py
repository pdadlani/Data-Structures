import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If inserting, we must already have a tree/root
        if self.value is None:
            self.value = value
            return self.value
        # If value is less than self.value, go left, make a new tree/node, if empty. Otherwise, keep going (recursion)
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        # If greater than or equal to self.value, go right, make a new tree/node, if empty. Otherwise, keep going (recursion)
        elif value >= self.value:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        if target == self.value:
            return True
        # otherwise, go left or right based on smaller or bigger
        elif target > self.value and self.right:
            # move right
            return self.right.contains(target)
        elif target < self.value and self.left:
            # move left
            return self.left.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # use recursion
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # research in order print to understand what it means
        # left, root, right
        if node.left:
            self.in_order_print(node.left)
        
        print(node.value)

        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Make a queue - FIFO
        queue = Queue()
        # add the root to the tail of the queue - default for a queue
        queue.enqueue(node)
        # while the queue is not empty
        while queue.len() > 0:
            # pop node off the front of the queue - which is default of the queue
            current_node = queue.dequeue()
            # cb or print node value OR DO THING
            print(current_node.value)
            # if node has left, add to tail of the queue
            if current_node.left:
                queue.enqueue(current_node.left)
            # if node has right, add to tail of the queue
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Make a stack - LIFO
        stack = Stack()
        # add the root to the head of stack - default for stack
        # while the stack is not empty
        # pop the node off the head of the stack - which is default for a stack
        # cb or print the value of the node or DO TH(ING)
        # if the node has a left, add the left to the stack
        # if the node has a right, add the right to the stack

        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        # root, left, right
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # left, right, root
        pass
