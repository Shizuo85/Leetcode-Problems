class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        s = (n+n*n)/2
        for i in nums:
            s-=i
        return s