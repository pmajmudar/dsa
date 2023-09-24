
class LinkedList:
  # Linkedin has:
  # fast insertion at start or end of List O(1)
  # Linear time for insert / delete / finding an item

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
  
  def insert(self, index):
    pass

  def find(self, index):
    cur_node = self.head
    for i in range(index):
      cur_node = cur_node.next
    return cur_node

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

  ll = LinkedList()
  ll.insert_start(n0)
  ll.insert_start(n1)
  ll.insert_start(n2)
  ll.insert_start(n3)
  print(ll)
  print(ll.find(2))