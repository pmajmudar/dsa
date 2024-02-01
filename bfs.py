import queue
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # only root node
        #if root.left is None and root.right is None:
        #    return 1
        q = queue.Queue()
        q.put(root)

        paths = {}
        paths[root] = [root.val]
        visited = {}
        good = 1

        while(not q.empty()):
            node = q.get()
            if node not in visited:
                visited[node] = True

                l = node.left
                r = node.right
                if l is not None:
                    if l.val >= max(paths[node]):
                        good += 1
                    paths[l] = paths[node] + [l.val]
                    q.put(l)

                if r is not None:
                    if r.val >= max(paths[node]):
                        good += 1
                    paths[r] = paths[node] + [r.val]
                    q.put(r)

        return good

