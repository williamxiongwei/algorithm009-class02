class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        queue = []

        for i, p in enumerate(prices):
            min_index, max_index = -1, -1
            if len(queue) > 0 and prices[queue[-1]] > p:
                res += prices[queue[-1]] - prices[queue[0]]
                queue = []

            queue.append(i)
        if len(queue) > 1:
            res += prices[queue[-1]] - prices[queue[0]]
        return res

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if not beginWord or not endWord or not wordList or len(beginWord) != len(endWord) or endWord not in wordList:
            return []

        res, visited, forward, backward, _len = [], set(), {beginWord: [[beginWord]]}, {endWord: [[endWord]]}, 2
        while forward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
            tmp = {}
            while forward:
                word, paths = forward.popitem()
                visited.add(word)
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new = word[:i] + c + word[i + 1:]
                        if new in backward:
                            if paths[0][0] == beginWord:
                                res.extend([fpath + bpath[::-1] for fpath in paths for bpath in backward[new]])
                            else:
                                res.extend([bpath + fpath[::-1] for fpath in paths for bpath in backward[new]])
                        if new in wordList and new not in visited:
                            tmp[new] = tmp.get(new, []) + [path + [new] for path in paths]
            _len += 1
            if res and _len > len(res[0]):
                break
            forward = tmp
        return res