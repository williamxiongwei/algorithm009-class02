class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        ret = 0
        '''
        left_max = [0 for x in height]
        for i in range(1, len(height)):
            if left_max[i-1] < height[i-1]:
                left_max[i] = height[i-1]
            else:
                left_max[i] = left_max[i-1]
        '''
        while l <= r:
            if left_max <= right_max:
                left_max = max(left_max, height[l])
                ret += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                ret += right_max - height[r]
                r -= 1
        return ret