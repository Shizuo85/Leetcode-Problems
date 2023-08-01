class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for i in nums:
            curr+=i
            if curr<1:
                ans+=1-curr
                curr=1
        return ans or 1