class Solution(object):
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        n = len(s)
        left, right = 0, n - 1
        for i in range(n):
            res += 1
            left, right = i - 1, i + 1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    res += 1
                    left, right = left - 1, right + 1
                else:
                    break
            left, right = i, i + 1
            while right < n:
                tmp = s[left:right + 1]
                if tmp == tmp[::-1]:
                    res += 1
                right += 2
        return res

    def minDistance(self, word1: str, word2: str) -> int:
        res = 0
        dp = [[float('inf') for _ in word2] for i in word1]
        n1, n2 = len(word1), len(word2)
        if n1 == 0 or n2 == 0:
            return max(n1, n2)

        for i in range(0, n1):
            for j in range(0, n2):
                if word1[i] != word2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
                    elif i > 0:
                        dp[i][j] = dp[i - 1][j] + 1
                    elif j > 0:
                        dp[i][j] = dp[i][j - 1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j - 1]
                    elif i > 0:
                        dp[i][j] = i
                    elif j > 0:
                        dp[i][j] = j
                    else:
                        dp[i][j] = 0
        return dp[n1 - 1][n2 - 1]