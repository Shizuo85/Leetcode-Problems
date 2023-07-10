class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return nums
        l=0
        r=1
        while r<len(nums):
            if nums[l]!=0:
                r+=1
                l+=1
            elif nums[r]!=0:
                nums[l], nums[r] = nums[r], nums[l]
                r+=1
                l+=1
            else:
                r+=1
        return nums
