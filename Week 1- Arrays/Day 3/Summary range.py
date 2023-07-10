class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans=[]
        if ans==nums: return ans
        l=0
        r=0
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                r+=1
                continue 
            else:
                if l==r:
                    ans.append(str(nums[r]))
                else:
                    ans.append(str(nums[l]) + "->" + str(nums[r]))
                r=l=i+1
        if l==r:

            ans.append(str(nums[r]))

        else:
            ans.append(str(nums[l]) + "->" + str(nums[r]))
            
        return ans


                
            
                
            