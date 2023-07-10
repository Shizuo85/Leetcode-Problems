class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst=[]
        one=0
        other=0
        ans=0
        for i in nums:
            if i==1:
                if other!=0:
                    lst.append(other)
                    other=0
                one+=1
            else:
                if one!=0:
                    ans=max(ans, one)
                    lst.append(one)
                    one=0
                other+=1
        if one!=0:
            ans=max(ans, one)
            lst.append(one)
            
        n=1
        if nums[0]==1:
            n=1
        else:
            n=2
        
        for k in range(n, len(lst)-1, 2):
            if lst[k]==1:
                ans= max(ans, lst[k-1]+lst[k+1])
        
        if ans == len(nums):
            ans-=1
        
        return ans
        
        
                    
        