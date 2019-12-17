"""Each ListNode holds a reference to its next node in the List."""

class sll_node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class SinglyLinkedList:
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
    new_node = sll_node(value, None)
    self.length += 1

    # If the list is empty
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node

  """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""
  def remove_from_head(self):
    if not self.head:
      return
    value = self.head.value
    self.delete(self.head)
    return value

  """Wraps the given value in a ListNode and inserts it 
  as the new tail of the list. Don't forget to handle 
  the old tail node's next pointer accordingly."""
  def add_to_tail(self, value):
    new_node = sll_node(value, None)
    self.length += 1

    # If list is empty
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  """Removes the List's current tail node, making the 
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""
  def remove_from_tail(self):
    if not self.tail:
      return
    value = self.tail.value
    self.delete(self.tail)
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
    value = node.value
    self.delete(node)
    self.add_to_tail(value)


  """Removes a node from the list and handles cases where
  the node was the head or the tail"""
  def delete(self, node):
    if not self.head and not self.tail:
      # TODO: This probably should not happen, handle error
      return
    self.length -= 1
    if self.head is self.tail:
      self.head = None
      self.tail = None
    elif self.head is node:
      self.head = node.next
      node.delete()
    elif self.tail is node:
      # self.tail = node.prev
      node.delete()
    else:
      node.delete()
      
  """Returns the highest value currently in the list"""
  def get_max(self):
    current = self.head
    max_value = current.value

    while current is not None:

      if current.value > max_value:
        max_value = current.value
      current = current.next

    return max_value

  def get_length(self):
    return self.length

  def get_middle(self):
    slower = self.head
    faster = self.head

    while faster.next and faster.next.next:
      slower = slower.next
      faster = faster.next.next

    return slower

  def printList(self): 
    temp = self.head 
    while(temp): 
        print(temp.value)
        temp = temp.next

trial = SinglyLinkedList()
trial.add_to_tail(3)
trial.add_to_tail(4)
trial.add_to_tail(5)
trial.add_to_tail(6)
trial.add_to_tail(7)
trial.add_to_tail(8)

print("LISTTTTTTTTTTTTTTT")
trial.printList()

a = trial.get_middle()
print(a.value)