class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        q = [i for i in range(1, n + 1)]

        def dfs(k, q, path):
            if k == 0:
                res.append(path)
                return

            for i, v in enumerate(q):
                tmp = q[i + 1:]

                dfs(k - 1, tmp, [v] if path is None else path + [v])

        dfs(k, q, None)
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(q, path):
            if not q or len(q) == 0:
                res.append(path)
                return
            for i, v in enumerate(q):
                tmp = q[:i] + q[i + 1:]
                dfs(tmp, [] if path is None else path + [q[i]])

        dfs(nums, [])
        return res