"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create the new node
        new_node = ListNode(value)
        # increment length
        self.length += 1
        # if the list is empty, aka no head or tail
        if not self.head and not self.tail:
            # then set the head and tail equal to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise, set
        else:
            # do the following in order! to not screw up your pointers / lose a node
            # the new node's next pointer equal to the current head
            new_node.next = self.head
            # the current head's previous pointer equal to the new node
            self.head.prev = new_node
            # the head equal to the new node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # if there is no head, aka empty
        if not self.head:
            return
        # new variable, removed_node, equal to the current head
        removed_node = self.head
        # delete the head
        self.delete(self.head)
        return removed_node.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # create a new node
        new_node = ListNode(value)
        # increment length
        self.length += 1
        # if the list is empty, aka no head and no tail
        if not self.head and not self.tail:
            # set head and tail equal to new node
            self.head = new_node
            self.tail = new_node
        # otherwise, set
        else:
            # the new node's previous pointer to the current tail
            new_node.prev = self.tail
            # the current tail's next pointer to the new node
            self.tail.next = new_node
            # the tail equal to the new node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # if no tail, aka empty list
        if not self.tail:
            return
        # new variable, equal to the current tail's value
        value = self.tail.value
        # delete the current tail
        self.delete(self.tail)
        # return the deleted value
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # if list is empty, return none?
        # decrement length
        self.length -= 1
        # if node not in list, return error message?
        # if it is the only node
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # else if node is head, do the stuff
        elif node is self.head:
            self.head = node.next
            node.delete()
        # else if node is tail, do the stuff
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # else just remove it
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # How to get max
        # create a max var
        current = self.head
        max = self.head.value
        # loop through nodes
        while current is not None:
            # compare value in node to max found
            if current.value > max:
                max = current.value
            current = current.next
        # return max found
        return max

    def get_length(self):
        return self.length