class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countMap = {}
        retList = []
        for n in nums:
            if n not in countMap:
                countMap[n] = 1
            else:
                countMap[n] += 1
        #sortedList = sorted(countMap.items(), key = lambda item: item[1], reverse=True)
        sortedList = [x[0] for x in sorted(countMap.items(), key = lambda item: item[1], reverse=True)]
        for key in sortedList:
            if len(retList) >= k:
                break
            retList.append(key)
        return retList