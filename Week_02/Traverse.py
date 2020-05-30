class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    import collections
    tree_deque = collections.deque()

    res = []
    head = root
    tree_deque.appendleft((head, 0))
    while len(tree_deque) > 0:
        head, flag = tree_deque.popleft()

        if flag == 0:
            tree_deque.appendleft((head, 1))
            curr = head.left
            while curr:
                tree_deque.appendleft((curr, 1))
                curr = curr.left
        elif flag == 1:
            # tree_deque.appendleft((head, 2))
            if head.right:
                tree_deque.appendleft((head.right, 0))
            res.append(head.val)

    return res

a = TreeNode(1)
b = TreeNode(3)
b.left = a
c = TreeNode(2)
c.left = b

inorderTraversal(c)