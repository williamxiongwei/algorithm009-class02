class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nLen = len(nums)
        if nLen == 0:
            return nLen
        prev = nums[0]
        i = 1
        while i < nLen:
            if nums[i] == prev:
                nums.pop(i)
                nLen -= 1
            else:
                prev = nums[i]
                i += 1
        return nLen