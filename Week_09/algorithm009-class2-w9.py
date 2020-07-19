class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[j == i for j in range(0, len(s))] for i in range(0, len(s))]
        nStart = 0
        nEnd = 0

        for i in range(1, len(s)):
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i - 1][j + 1] or (i - j == 1)
                    if dp[i][j] and (nEnd - nStart) < (i - j):
                        nStart = j
                        nEnd = i
        return s[nStart: nEnd+1]

    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        n = len(s)
        maxl = 0
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] + 2) if i >= 2 else 2
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                        dp[i] = (dp[i - 1] + dp[i - dp[i - 1] - 2] + 2) if i - dp[i - 1] >= 2 else dp[i - 1] + 2
                maxl = max(maxl, dp[i])
        return maxl