class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums)-2, 3):
            if nums[i]==nums[i+2]:
                continue 
            else:
                return nums[i]
        return nums[-1]