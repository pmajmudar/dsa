
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def construct_tree(nodes):
    root = Node(nodes[0])
    tree = [root]

    for i in range(1, len(nodes)):
        parent_idx = (i - 1) // 2
        #print(parent_idx)
        parent = tree[parent_idx]
        if i % 2:
           parent.left = Node(nodes[i])
           tree.append(parent.left)
        else:
           parent.right = Node(nodes[i])
           tree.append(parent.right)

    return root

def traverse(node):
    """In-order traversal"""
    if node is None:
       return
    traverse(node.left)
    print(node.val)
    traverse(node.right)

def pre_order(node):
    if node is None:
        return
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)


nodes = [1, 2, 3, None, 5, None, 4]
tree = construct_tree(nodes)

print("Traversing tree in-order")
traverse(tree)

print("\n\nPre-order:")
pre_order(tree)

