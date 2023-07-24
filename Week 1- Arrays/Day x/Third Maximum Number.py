class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = float("-inf")
        second = float("-inf")
        third = float("-inf")
        
        nums=set(nums)
        for i in nums:
            if i>first:
                third=second
                second=first
                first=i
            elif i>second:
                third=second
                second=i
            elif i>third:
                third=i
        return third if third != float("-inf") else first