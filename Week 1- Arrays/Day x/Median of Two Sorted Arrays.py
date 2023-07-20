class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = 0
        n=0
        count = 0
        curr = 0
        prev=0
        mid = (len(nums1)+len(nums2))//2
        
        while count< mid+1:
            if n>=len(nums2):
                prev=curr
                curr = nums1[m]
                m+=1
            elif m>=len(nums1):
                prev=curr
                curr=nums2[n]
                n+=1
            elif nums1[m]<nums2[n]:
                prev=curr
                curr = nums1[m]
                m+=1
            else:
                prev=curr
                curr=nums2[n]
                n+=1
            count+=1
        
        return curr if (len(nums1)+len(nums2))%2!=0 else (prev+curr)/2
        