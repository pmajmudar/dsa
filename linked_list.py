
class LinkedList:
  # Linkedin has:
  # fast insertion at start or end of List O(1)
  # Linear time for insert / delete / finding an item

  # Potential issue is cycles in a Linkedin List - causes never ending loops
  # --> Could be solved by using a hashset and following the list - add a node
  # to set if seen. O(N) Time and O(N) space.
  # OR use two pointers (Fast + slow) - Floyd... algo - eventually both are
  # caught in the loop - if they are equal - we have a loop OR if fast ptr
  # just gets to end - then we don't have a loop.

  def __init__(self):
    self.head = None
    self.tail = None

  # def insert_end(self, node):
  #   if self.tail is None:
  #     self.head = node
  #     self.tail = node
  #     return

  #   self.tail.next = node

  def delete(self, index):
    if index == 0:
      self.head = self.head.next
    else:
      prev = self.find(index - 1)
      #prev.next = prev.next.next

  def insert_start(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
      return

    node.next = self.head
    self.head = node

  def insert(self, index, node):
    if index == 0:
      return self.insert_start(node)

    cur_node = self.head
    for i in range(index - 1):
      if cur_node.next is None:
        raise IndexError
      cur_node = cur_node.next

    node.next = cur_node.next
    cur_node.next = node

  def find(self, index):
    cur_node = self.head
    for i in range(index):
      cur_node = cur_node.next
    return cur_node

  # def find_node(self, node):
  #   if node.next is None:
  #     return node
  #   return find_node(node.next)

  def __repr__(self):
    cur_node = self.head
    out = str(cur_node.data)

    while cur_node.next is not None:
      cur_node = cur_node.next
      out += f", {cur_node.data}"
    return out


class ListNode:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    return f"<{self.data}>"



if __name__ == "__main__":
  n0 = ListNode('A')
  n1 = ListNode('B')
  n2 = ListNode('C')
  n3 = ListNode('D')
  n4 = ListNode('Test')

  ll = LinkedList()
  ll.insert_start(n0)
  ll.insert_start(n1)
  ll.insert_start(n2)
  ll.insert_start(n3)
  ll.insert(2, n4)
  print(ll)
  print(ll.find(2))
  #print(ll.find_node(self.head))
