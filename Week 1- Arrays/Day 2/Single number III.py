class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans=[]
        n=0
        while n<len(nums)-1:
            if nums[n] == nums[n+1]:
                n+=2
            else:
                ans.append(nums[n])
                n+=1
            if len(ans)==2:
                return ans
        return ans + [nums[-1]]