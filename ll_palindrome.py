from linked_list import ListNode


palin = 'abcba'

prev = None
nodes = []
for char in palin:
    n  = ListNode(char)
    nodes.append(n)
    if prev is not None:
        prev.next = n
    prev = n

print(nodes)

def check_palin(head):
    fast = head
    slow = head

    stack = []
    while fast.next and fast.next.next:
        stack.append(slow)
        slow = slow.next
        fast = fast.next.next

    print(stack)

    is_odd = False
    if fast.next is None:
        is_odd = True

    if is_odd:
        slow = slow.next

    while slow:
        n = stack.pop()
        print(n, " vs ", slow.data)
        if n.data != slow.data:
            print("Not a palindrome")
            break
        slow = slow.next

    if len(stack) == 0:
        print("Is a palindrome")

check_palin(nodes[0])
