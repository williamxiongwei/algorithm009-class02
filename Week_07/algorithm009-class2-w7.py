class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, path):
            if left == n and right == n:
                res.append(path)
                return
            if right > left:
                return
            if left < n:
                dfs(left+1, right, path+"(")
            if right < n:
                dfs(left, right+1, path+")")
        dfs(0, 0, "")
        return res

    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    dfs(queens + [q], xy_diff + [p - q], xy_sum + [p + q])

        res = []
        dfs([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in r] for r in res]