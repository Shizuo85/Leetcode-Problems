class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst1=Counter(nums1)
        lst2=Counter(nums2)
        ans=[]
        
        for i in lst1:
            if i in lst2:
                ans+= min(lst1[i],lst2[i]) * [i]
        return ans