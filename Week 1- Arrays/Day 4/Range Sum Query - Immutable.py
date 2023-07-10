class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
        return self.nums[right] if left==0 else self.nums[right]-self.nums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)