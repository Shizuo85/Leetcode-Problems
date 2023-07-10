class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)/2
        dct={}

        for i in nums:
            if i in dct:
                dct[i] = dct[i] + 1
            else:
                dct[i] = 1
            if dct[i]>n:
                return i