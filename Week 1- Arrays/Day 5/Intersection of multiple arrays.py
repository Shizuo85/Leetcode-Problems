class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        curr = set(nums[0])
        for i in range(1, len(nums)):
            curr = curr & set(nums[i])
        return sorted(list(curr))