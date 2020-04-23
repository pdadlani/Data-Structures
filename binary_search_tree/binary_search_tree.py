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
        # if node.value == target:
        if self.value == target:
            # return true
            return True
        # otherwise, if target is < node.value AND there is a left:
        elif target < self.value and self.left:
            # find the target on left bst
            return self.left.contains(target)
        # else if target is >= node.value AND there is a right:
        elif target > self.value and self.right:
            # find the target on the right bst
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if tree is empty, return None
        if self.value is None:
            return None
        # if self.right is None, return self.value
        if self.right is None:
            return self.value
        # else call get_max on self.right
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # if there is a root, call cb on that root
        if self.value:
            cb(self.value)
        # if there is a left, call for each on the left, with cb passed in
        if self.left:
            self.left.for_each(cb)
        # if there is a right, call for each on the right, with cb passed in
        if self.right:
            self.right.for_each(cb)

    def depth_first_iterative_for_each(self, cb):
        stack = []
        # add the root of the tree to the stack
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current_node = stack.pop()
            # check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
            # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def breadth_first_iterative_for_each(self, cb):
        # depth-first : stack
        # breadth-first : queue
        q = Queue()
        q.enqueue(self)

        while len(q) > 0:
            current_node = q.dequeue()
            if current_node.left:
                q.enqueue(current_node.left)
            if current_node.right:
                q.enqueue(current_node.right)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # print left, root, then right
        # if there is a left, traverse the left
        if node.left:
            self.in_order_print(node.left)
        # then print the 'root'
        print(node.value)
        # if there is a right, traverse the right
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # FIFO aka a queue
        # instantiate a queue
        queue = Queue()
        # add the node to the queue
        queue.enqueue(node)

        # while the length of the queue is not 0
        while queue.len() > 0:
            # remove the first node from queue
            current_node = queue.dequeue()
            # print the value of the node
            print(current_node.value)
            # if node has a left
            if current_node.left:
                # add the left to the queue
                queue.enqueue(current_node.left)
            # if the node has a right,
            if current_node.right:
                # add the right to the queue
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # FILO aka a stack
        # instantiate a stack
        stack = Stack()
        # add the node to the stack
        stack.push(node)

        # while the length of the stack is not 0
        while stack.len() > 0:
            # remove the first node from the stack
            current_node = stack.pop()
            # print the value of the node
            print(current_node.value)
            # if node has a left
            if current_node.left:
                # add the left to the stack
                stack.push(current_node.left)
            # if the node has a right
            if current_node.right:
                # add the right to the stack
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # root, left, then right
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # left, right, then root
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)


# bst = BinarySearchTree(7)
# bst.insert(5)
# bst.insert(8)
# bst.insert(4)
# bst.insert(6)
# bst.get_max()

bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.in_order_print(bst)
