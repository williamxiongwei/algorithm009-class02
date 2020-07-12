class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for q in range(n):
                if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    dfs(queens+[q], xy_diff+[p-q], xy_sum+[p+q])
        res = []
        dfs([],[],[])
        return [["."*i + "Q" + "."*(n-i-1) for i in r] for r in res]

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0